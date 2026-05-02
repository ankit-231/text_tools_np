"""
To send a text via an endpoint and return the response
"""

import re

from bs4 import BeautifulSoup

from app.segmenter import segment_text
from app.sender import UNICODE_TO_PREETI_CONVERTER_URL
from app.session import get_session

PLACEHOLDER_PATTERN = re.compile(r"XKEEPX([A-Z]+)XKEEPX")


# Replace key generation in _build_payload
def _int_to_letters(n: int) -> str:
    """Encode an integer as letters only: 0→A, 1→B, …, 26→AA, 27→AB …"""
    result = ""
    n += 1
    while n:
        n, rem = divmod(n - 1, 26)
        result = chr(65 + rem) + result
    return result


def _build_payload(content: str) -> tuple[str, dict[str, str]]:
    """
    Replace every non-Nepali segment with a placeholder like ###0###.

    Returns:
        masked_text  - the content safe to send to the converter
        placeholders - mapping of "###N###" → original segment
    """
    placeholders = {}
    parts = []
    counter = 0

    for chunk, is_nepali in segment_text(content):
        if is_nepali:
            parts.append(chunk)
        else:
            key = f"XKEEPX{_int_to_letters(counter)}XKEEPX"
            placeholders[key] = chunk
            parts.append(key)
            counter += 1

    return "".join(parts), placeholders


def _restore_placeholders(preeti_text: str, placeholders: dict[str, str]) -> str:
    """Substitute every ###N### back with its original segment."""
    return PLACEHOLDER_PATTERN.sub(lambda m: placeholders[m.group(0)], preeti_text)


def send_page_in_one_go(content: str) -> str:
    """
    Convert a full page of mixed Nepali/English text in one POST request.
    """
    masked_text, placeholders = _build_payload(content)

    # If there's nothing Nepali at all, skip the network call entirely
    if not placeholders or len(placeholders) == len(list(segment_text(content))):
        return content

    session = get_session()
    payload = {"userInput": masked_text, "output": ""}
    response = session.post(UNICODE_TO_PREETI_CONVERTER_URL, data=payload)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")
    textarea = soup.find("textarea", class_="out preeti")
    if textarea is None:
        raise ValueError("Could not find Preeti output textarea in response HTML.")

    preeti_text = textarea.text
    return _restore_placeholders(preeti_text, placeholders)


if __name__ == "__main__":
    sample = "Invoice No: 123  थिति स्थिति  Amount: Rs. १२१४  राम शाहको थितिहरु।"
    print(send_page_in_one_go(sample))
    pass

"""
To send a text via an endpoint and return the response
"""

from bs4 import BeautifulSoup
from requests import Session

from app.segmenter import segment_text

UNICODE_TO_PREETI_CONVERTER_URL = "https://unicode.shresthasushil.com.np/"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept": "text/html,application/json",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
}


def get_session():
    session = Session()
    session.headers.update(HEADERS)
    return session


def _convert_nepali_chunk(content: str, session: Session) -> str:
    """Send a purely-Nepali chunk and return the Preeti result."""
    payload = {"userInput": content, "output": ""}
    response = session.post(UNICODE_TO_PREETI_CONVERTER_URL, data=payload)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")
    textarea = soup.find("textarea", class_="out preeti")
    if textarea is None:
        raise ValueError("Could not find Preeti output textarea in response HTML.")
    return textarea.text


def send_page(content: str) -> str:
    """
    Convert a page of mixed Nepali/English text.

    - Nepali (Devanagari) segments are sent to the unicode→Preeti converter.
    - All other segments (English, numbers, punctuation …) are kept as-is.

    Returns the fully reassembled converted string.
    """
    session = get_session()
    result_parts = []

    total_requests_made = 0

    for chunk, is_nepali in segment_text(content):
        if is_nepali:
            # print(chunk)
            converted = _convert_nepali_chunk(chunk, session)
            total_requests_made += 1
            result_parts.append(converted)
        else:
            result_parts.append(chunk)  # pass through unchanged

    # print("Total requests made:", total_requests_made)
    return "".join(result_parts)


if __name__ == "__main__":
    # content = "थिति स्थिति  प्रबन्ध राम शाहको थितिहरु"
    # converted = send_page(content=content)
    # print(converted)
    sample = "Invoice No: 123  थिति स्थिति  Amount: Rs. १२१४  राम शाहको थितिहरु।"
    print(send_page(sample))

    pass

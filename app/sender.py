"""
To send a text via an endpoint and return the response
"""

from requests import Session

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


def send_page(content):
    url = UNICODE_TO_PREETI_CONVERTER_URL
    payload = {"userInput": content, "output": ""}
    session = get_session()
    # response = session.post(url, json=payload)
    response = session.post(url, data=payload)
    response.raise_for_status()
    resp_text = response.text

    # output_html_path = "files/output.html"
    # with open(output_html_path, "w", encoding="utf-8") as file:
    #     file.write(resp_text)

    return resp_text


if __name__ == "__main__":
    # content = "थिति स्थिति  प्रबन्ध राम शाहको थितिहरु"
    # converted = send_page(content=content)
    # print(converted)
    pass

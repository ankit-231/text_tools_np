from requests import Session

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

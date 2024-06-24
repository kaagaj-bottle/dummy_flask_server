import requests
import uuid
from typing import Dict, List
from app.connections import r_conn, queue


def fetch_urls_from_db(user_id: str) -> List[str]:
    urls = r_conn.lrange(user_id, 0, -1)
    urls = [url.decode("utf-8") for url in urls]
    return urls


def fetch_url_text_from_db(url) -> str:
    url_text = r_conn.get(url)
    url_text = url_text.decode("utf-8")
    return url_text


def push_url_text_from_web(url: str):
    url_text = requests.get(url).text
    return url_text

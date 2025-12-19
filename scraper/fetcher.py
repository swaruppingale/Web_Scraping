import requests
import time
from scraper.config import HEADERS, REQUEST_DELAY

def fetch_page(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        time.sleep(REQUEST_DELAY)
        return response.text
    except requests.RequestException as e:
        print(f"[ERROR] Failed to fetch {url}: {e}")
        return None

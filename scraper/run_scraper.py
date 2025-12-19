import pandas as pd
from scraper.fetcher import fetch_page
from scraper.parser import parse_article
from scraper.keyword_detector import detect_exploit_status
from scraper.change_detector import is_content_changed

URLS = [
    "https://blog.rapid7.com/",
    "https://security.googleblog.com/"
]

results = []

for url in URLS:
    html = fetch_page(url)
    if not html:
        continue

    if not is_content_changed(url, html, "data/previous_snapshot.json"):
        continue

    parsed = parse_article(html)
    exploit_status = detect_exploit_status(parsed["text"])

    results.append({
        "source": url,
        "cves": ", ".join(parsed["cves"]),
        "exploit_status": exploit_status
    })

df = pd.DataFrame(results)
df.to_csv("data/extracted_exploits.csv", index=False)

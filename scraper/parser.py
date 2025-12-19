from bs4 import BeautifulSoup
import re

def parse_article(html):
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text(separator=" ", strip=True)

    cve_matches = re.findall(r"CVE-\d{4}-\d{4,7}", text)

    return {
        "text": text,
        "cves": list(set(cve_matches))
    }

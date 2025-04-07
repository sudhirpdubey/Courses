import requests
from bs4 import BeautifulSoup
import random
import time

def smart_delay(min_delay=1, max_delay=3):
    delay = random.uniform(min_delay, max_delay)
    time.sleep(delay)

def detect_selectors(soup):
    data = []

    # Extract tables
    for table in soup.find_all("table"):
        headers = []
        header_row = table.find("tr")
        if header_row:
            headers = [th.get_text(strip=True) for th in header_row.find_all(["th", "td"])]
        for row in table.find_all("tr")[1:]:
            cells = [td.get_text(strip=True) for td in row.find_all(["td", "th"])]
            if cells:
                record = dict(zip(headers, cells)) if headers else {"row": cells}
                data.append(record)

    # Extract lists
    for ul in soup.find_all(["ul", "ol"]):
        items = [li.get_text(strip=True) for li in ul.find_all("li")]
        if items:
            data.append({"list_items": items})

    # Extract definition lists
    for dl in soup.find_all("dl"):
        dts = dl.find_all("dt")
        dds = dl.find_all("dd")
        if dts and dds and len(dts) == len(dds):
            record = {dt.get_text(strip=True): dd.get_text(strip=True) for dt, dd in zip(dts, dds)}
            data.append(record)

    # Fallback: extract paragraphs and headings
    for tag in soup.find_all(["p", "h1", "h2", "h3", "h4", "h5", "h6"]):
        text = tag.get_text(strip=True)
        if text:
            data.append({"tag": tag.name, "text": text})

    return data
    return data

def scrape_single_page(url):
    headers = {
        "User-Agent": random.choice([
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
            "Mozilla/5.0 (X11; Linux x86_64)"
        ])
    }
    smart_delay()
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    data = detect_selectors(soup)
    return data

def scrape_website(url, mode="Single Page", max_pages=5):
    if mode == "Single Page":
        return scrape_single_page(url)

    elif mode == "Multiple Pages":
        all_data = []
        current_url = url
        for _ in range(max_pages):
            headers = {
                "User-Agent": random.choice([
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
                    "Mozilla/5.0 (X11; Linux x86_64)"
                ])
            }
            smart_delay()
            response = requests.get(current_url, headers=headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            page_data = detect_selectors(soup)
            all_data.extend(page_data)

            # Find next page link
            next_link = soup.find("a", string=lambda t: t and "next" in t.lower())
            if next_link and next_link.get("href"):
                next_url = next_link["href"]
                if not next_url.startswith("http"):
                    from urllib.parse import urljoin
                    next_url = urljoin(current_url, next_url)
                current_url = next_url
            else:
                break
        return all_data

    elif mode == "Whole Website":
        # Placeholder: implement recursive crawl
        return scrape_single_page(url)

    elif mode in ["Instagram", "YouTube", "Hashtag", "Niche", "Account"]:
        # Placeholder: implement social media scraping
        return scrape_single_page(url)

    else:
        return scrape_single_page(url)
import argparse
import json
import os
from scraper.content_scraper import scrape_all_sources
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    parser = argparse.ArgumentParser(description="Content Research & Scraping CLI")
    parser.add_argument("--output", type=str, default="outputs/trending_topics.json", help="Output JSON file path")
    args = parser.parse_args()

    logging.info("Starting content scraping...")
    data = scrape_all_sources()

    # Ensure output directory exists
    os.makedirs(os.path.dirname(args.output), exist_ok=True)

    # Save to JSON
    try:
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        logging.info(f"Scraping completed. Data saved to {args.output}")
    except Exception as e:
        logging.error(f"Failed to save JSON: {e}")

if __name__ == "__main__":
    main()
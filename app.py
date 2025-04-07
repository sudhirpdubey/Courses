import streamlit as st
from scraper.core import scrape_website
import json
import pandas as pd
import os
import time

st.title("SmartScraperApp - Intelligent Web Scraper")

st.sidebar.header("Scraping Options")

url = st.sidebar.text_input("Enter URL to scrape", "")

mode = st.sidebar.selectbox("Scraping Mode", ["Single Page", "Multiple Pages", "Whole Website", "Instagram", "YouTube", "Hashtag", "Niche", "Account"])

output_format = st.sidebar.multiselect("Output Format", ["JSON", "Excel"], default=["JSON", "Excel"])

start_button = st.sidebar.button("Start Scraping")

if start_button and url:
    # Ensure outputs directory exists
    os.makedirs("outputs", exist_ok=True)
    st.write(f"Starting scrape for: {url} in mode: {mode}")
    with st.spinner("Scraping in progress..."):
        try:
            data = scrape_website(url, mode)
            timestamp = int(time.time())
            if "JSON" in output_format:
                json_path = os.path.join("outputs", f"scrape_{timestamp}.json")
                abs_json_path = os.path.abspath(json_path)
                try:
                    with open(abs_json_path, "w", encoding="utf-8") as f:
                        json.dump(data, f, ensure_ascii=False, indent=2)
                    st.success(f"JSON saved to {abs_json_path}")
                except Exception as e:
                    st.error(f"Failed to save JSON: {e}")
                st.success(f"JSON saved to {json_path}")
            if "Excel" in output_format:
                excel_path = os.path.join("outputs", f"scrape_{timestamp}.xlsx")
                df = pd.DataFrame(data)
                df.to_excel(excel_path, index=False)
                st.success(f"Excel saved to {excel_path}")
            st.write("Sample Data:", data[:5])
        except Exception as e:
            st.error(f"Error during scraping: {e}")
else:
    st.write("Enter a URL and click 'Start Scraping' to begin.")
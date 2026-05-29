"""
Google Hotels API: A Quick Start Example
See more at: https://apify.com/johnvc/google-hotels-search-scraper?fpr=9n7kx3
Input schema: https://apify.com/johnvc/google-hotels-search-scraper/input-schema?fpr=9n7kx3

This script shows how to call the Google Hotels API on Apify from Python and read
its structured JSON output. It exercises several input parameters so you can see
what is configurable, while keeping the run small so your first call stays cheap.

Get your free Apify API key at: https://apify.com?fpr=9n7kx3
"""

import os
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()

# Initialize the Apify client with your API token (read from .env)
client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

# Build the Actor input.
# max_pages is kept at 1 to keep this first run inexpensive (each page is billed
# separately). Raise it once you have your own API key and know your budget.
run_input = {
    "q": "hotels in Paris",
    "gl": "us",                      # country code
    "hl": "en",                      # language code
    "currency": "USD",
    "check_in_date": "2026-06-29",   # YYYY-MM-DD
    "check_out_date": "2026-07-01",  # YYYY-MM-DD
    "adults": 2,
    "max_pages": 1,
}

# Run the Actor and wait for it to finish
run = client.actor("johnvc/google-hotels-search-scraper").call(run_input=run_input)
if run is None:
    raise SystemExit("The Actor run did not return a result.")

# Read structured results from the run's default dataset (one item per page)
items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"Returned {len(items)} page(s) of results.\n")

# Show a few hotels from each page.
for item in items:
    meta = item.get("search_metadata", {})
    print(f"Properties found: {meta.get('properties_count')}")
    for prop in (item.get("properties") or [])[:5]:
        rate = (prop.get("rate_per_night") or {}).get("lowest")
        print(f"  {prop.get('name')}  |  {rate} per night  |  {prop.get('type')}")
    print()

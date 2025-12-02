"""
Google Hotels API: A Quick Start Example
See more at: https://apify.com/johnvc/google-hotels-search-scraper?fpr=9n7kx3

This script demonstrates how to use the Google Hotels API Actor
to search Google Hotels and retrieve structured hotels data.
"""

import os
from typing import Dict, Any, Optional
from dotenv import load_dotenv
from apify_client import ApifyClient
import rich

load_dotenv()

# Initialize the ApifyClient with your API token
client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

# Prepare the Actor input
run_input = {
    "q": "hotels in New York City",
    "gl": "us",
    "hl": "en",
    "currency": "USD",
    "check_in_date": "2026-12-13",
    "check_out_date": "2026-12-14",
    "max_pages": 1
}


for page in range(1, 2):
    run_input["max_pages"] = page
    # Run the Actor and wait for it to finish
    run = client.actor("johnvc/google-hotels-search-scraper").call(run_input=run_input)
    
    # Fetch and print Actor results from the run's dataset (if there are any)
    rich.print("💾 Check your data here: https://console.apify.com/storage/datasets/" + run["defaultDatasetId"])
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        rich.print(item)
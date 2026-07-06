"""
Google Hotels API: Autocomplete Suggestions Example
See more at: https://apify.com/johnvc/google-hotels-search-scraper?fpr=9n7kx3
Input schema: https://apify.com/johnvc/google-hotels-search-scraper/input-schema?fpr=9n7kx3

Autocomplete mode turns a full or partial query into the suggestions Google
Hotels shows while you type: destinations, regions, and specific hotels.
Suggestions for specific hotels include a property_token, which you can feed
straight into the photos, reviews, or property-details modes (see the
google-hotels-photos.py and google-hotels-reviews.py examples).

Get your free Apify API key at: https://apify.com?fpr=9n7kx3
"""

import os
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()

# Initialize the Apify client with your API token (read from .env)
client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

# Autocomplete needs only a query. Partial queries work well.
run_input = {
    "search_type": "autocomplete",
    "q": "hotels in par",
    "gl": "us",   # country code
    "hl": "en",   # language code
}

# Run the Actor and wait for it to finish
run = client.actor("johnvc/google-hotels-search-scraper").call(run_input=run_input)
if run is None:
    raise SystemExit("The Actor run did not return a result.")

# One dataset item per suggestion
items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"Returned {len(items)} suggestion(s) for '{run_input['q']}'.\n")

for item in items:
    token = item.get("property_token")
    marker = f"  ->  property_token: {token}" if token else ""
    print(f"{item.get('position'):>2}. {item.get('value')}  ({item.get('suggestion_type')}){marker}")

print(
    "\nTip: suggestions with a property_token are specific hotels. Chain that token\n"
    "into search_type='photos' or search_type='reviews' to pull their galleries and\n"
    "guest reviews. Try a hotel-name query like 'Marriott Marquis Times Square'."
)

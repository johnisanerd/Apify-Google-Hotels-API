"""
Google Hotels API: Property Photos Example
See more at: https://apify.com/johnvc/google-hotels-search-scraper?fpr=9n7kx3
Input schema: https://apify.com/johnvc/google-hotels-search-scraper/input-schema?fpr=9n7kx3

Photos mode returns the complete photo gallery for one property: full-size and
thumbnail URLs, gallery sections ("At a glance", "Rooms", ...), dimensions, and
sources. It needs a property_token, so this example chains two runs:

  1. autocomplete mode on a hotel name  ->  property_token
  2. photos mode on that token          ->  one dataset item per photo

Get your free Apify API key at: https://apify.com?fpr=9n7kx3
"""

import os
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()

# Initialize the Apify client with your API token (read from .env)
client = ApifyClient(os.getenv("APIFY_API_TOKEN"))
actor = client.actor("johnvc/google-hotels-search-scraper")

HOTEL_NAME = "Marriott Marquis Times Square"

# --- Step 1: resolve the hotel name into a property_token via autocomplete ---
run = actor.call(run_input={"search_type": "autocomplete", "q": HOTEL_NAME})
if run is None:
    raise SystemExit("The autocomplete run did not return a result.")

suggestions = list(client.dataset(run.default_dataset_id).iterate_items())
property_token = next((s.get("property_token") for s in suggestions if s.get("property_token")), None)
if not property_token:
    raise SystemExit(f"No property_token found for '{HOTEL_NAME}'. Try a more specific hotel name.")
print(f"Resolved '{HOTEL_NAME}' -> property_token {property_token}\n")

# --- Step 2: fetch the photo gallery for that property ---
run = actor.call(run_input={
    "search_type": "photos",
    "property_token": property_token,
    "max_pages": 1,   # one photos page typically returns 100-200 photos
})
if run is None:
    raise SystemExit("The photos run did not return a result.")

photos = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"Returned {len(photos)} photo(s).\n")

# Group a preview by gallery section
sections = {}
for photo in photos:
    sections.setdefault(photo.get("section_title") or "Other", []).append(photo)

for section, section_photos in sections.items():
    print(f"{section}: {len(section_photos)} photo(s)")
    for photo in section_photos[:2]:
        print(f"   {photo.get('photo_url')}")
print("\nEach dataset item carries photo_url, thumbnail_url, dimensions, and source.")

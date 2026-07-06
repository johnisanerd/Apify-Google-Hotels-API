"""
Google Hotels API: Guest Reviews Example
See more at: https://apify.com/johnvc/google-hotels-search-scraper?fpr=9n7kx3
Input schema: https://apify.com/johnvc/google-hotels-search-scraper/input-schema?fpr=9n7kx3

Reviews mode returns paginated guest reviews for one property: rating, text,
date, source platform, reviewer details, subratings, and the hotel's response.
It needs a property_token, so this example chains two runs:

  1. autocomplete mode on a hotel name  ->  property_token
  2. reviews mode on that token         ->  one dataset item per review

Sort options (reviews_sort_by): "1" most helpful (default), "2" most recent,
"3" highest score, "4" lowest score.

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

# --- Step 2: fetch the most recent guest reviews, two pages deep ---
run = actor.call(run_input={
    "search_type": "reviews",
    "property_token": property_token,
    "reviews_sort_by": "2",   # most recent first
    "max_pages": 2,           # ~10 reviews per page
})
if run is None:
    raise SystemExit("The reviews run did not return a result.")

reviews = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"Returned {len(reviews)} review(s), most recent first.\n")

for review in reviews[:8]:
    stars = "*" * int(review.get("rating") or 0)
    snippet = (review.get("review_snippet") or "(rating only, no text)").strip()
    if len(snippet) > 90:
        snippet = snippet[:87] + "..."
    print(f"{stars:<5} {review.get('review_date'):<15} {review.get('review_source'):<12} {snippet}")

print("\nEach dataset item carries the full review object: subratings, images,")
print("hotel highlights, and the property's response when one exists.")

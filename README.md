[# Google Hotels API](https://apify.com/johnvc/google-hotels-search-scraper?fpr=9n7kx3)

## 🏨 Google Hotels Search API

> **The most powerful, reliable, and feature‑rich Google Hotels search API.**

You can run this using pay‑per‑event pricing on Apify here:  
[https://apify.com/johnvc/google-hotels-search-scraper](https://apify.com/johnvc/google-hotels-search-scraper?fpr=9n7kx3)

### 🚀 Quick Start

#### Prerequisites
- Python 3.8 or higher
- An Apify account and API key

#### Setup Instructions

1. **Clone the repository**

```bash
git clone <your-repo-url>
cd Apify-Google-Hotels-API
```

2. **Create and activate a virtual environment (using `uv`, recommended)**

```bash
# Create a virtual environment
uv venv

# Activate the virtual environment
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate
```

3. **Install dependencies**

```bash
uv pip install -r requirements.txt
```

4. **Configure your API key**

```bash
# Copy the example environment file if present, or create .env
cp .env.example .env  # if .env.example exists

# Then edit .env and add your Apify API key
# APIFY_API_TOKEN=your_api_key_here
```

You can get your API token from your Apify account dashboard:  
[https://apify.com](https://apify.com?fpr=9n7kx3)

5. **Run the example**

```bash
python google-hotels-api.py
```

#### Alternative: Direct API key usage

If you prefer not to use a `.env` file, you can set the environment variable directly:

```bash
export APIFY_API_TOKEN="your_api_key_here"
python google-hotels-api.py
```

On Windows (PowerShell):

```powershell
$Env:APIFY_API_TOKEN="your_api_key_here"
python google-hotels-api.py
```

---

## 💡 What is Google Hotels Search Scraper?

The Google Hotels Search Scraper is a smart automation tool that extracts hotel listings, prices, ratings, amenities, images, and detailed property information from Google Hotels, returning clean structured data (JSON, CSV, Excel, etc.) for direct use in your applications or data pipelines.  
It is ideal for market research, price monitoring, competitive analysis, building travel apps, and generating SEO‑optimized hotel content using real‑time Google Hotels data.  

Key benefits:
- Turn Google Hotels into a structured dataset for analytics and automation.
- Power hotel comparison tools, travel search, and pricing intelligence.
- Export results via Apify datasets as JSON, CSV, or Excel.

For full feature documentation, configuration options, and examples, see the Apify Actor page:  
[https://apify.com/johnvc/google-hotels-search-scraper](https://apify.com/johnvc/google-hotels-search-scraper?fpr=9n7kx3)

---

## 📦 Example Input Payloads

Below are some example inputs you can use when running the Actor directly on Apify or via API.

### Example 0: Basic Search (Hotels in Paris)

```json
{
  "q": "hotels in Paris",
  "check_in_date": "2025-12-13",
  "check_out_date": "2025-12-14",
  "adults": 2,
  "max_pages": 1
}
```

### Example 1: Search with Dates and Guests

```json
{
  "q": "Bali Resorts",
  "check_in_date": "2025-12-13",
  "check_out_date": "2025-12-14",
  "adults": 2,
  "children": 0,
  "currency": "USD",
  "max_pages": 1
}
```

### Example 2: Search with Filters (Price, Stars, Amenities, Property Types)

```json
{
  "q": "hotels in New York",
  "check_in_date": "2025-12-13",
  "check_out_date": "2025-12-14",
  "adults": 2,
  "min_price": "100",
  "max_price": "300",
  "stars": "4,5",
  "amenities": "35,40",
  "property_type": "17,18",
  "currency": "USD",
  "max_pages": 1
}
```

### Example 3: Vacation Rentals Search

```json
{
  "q": "vacation rentals in Miami",
  "check_in_date": "2025-12-13",
  "check_out_date": "2025-12-20",
  "adults": 4,
  "children": 2,
  "children_ages": "5,8",
  "vacation_rentals": true,
  "bedrooms": 2,
  "bathrooms": 2,
  "currency": "USD",
  "max_pages": 1
}
```

### Example 4: Property Details (using `property_token`)

```json
{
  "property_token": "ChYIq6y...",
  "max_pages": 1
}
```

See the Actor README for full filter ID references, parameter validation rules, and advanced usage:  
[https://apify.com/johnvc/google-hotels-search-scraper](https://apify.com/johnvc/google-hotels-search-scraper?fpr=9n7kx3)

---

## 🔄 How the Example Script Works

The included `google-hotels-api.py` script:
- Loads your `APIFY_API_TOKEN` from the environment (using `python-dotenv` if available).
- Initializes an `ApifyClient`.
- Calls the `johnvc/google-hotels-search-scraper` Actor with a sample search (hotels in South Bend, Indiana).
- Iterates over the resulting dataset and prints items using `rich` for readable output.

You can customize the `run_input` dictionary in `google-hotels-api.py` to match any of the examples above or your own search parameters.

For the Apify Python client docs, see:  
[https://docs.apify.com/sdk/python](https://docs.apify.com/sdk/python)

---

## 🧾 Output and Export

The scraper stores results in an Apify dataset.  
From the console link printed by the script (e.g. `https://console.apify.com/storage/datasets/<DATASET_ID>`), you can:
- Inspect results in the Apify UI.
- Download them as JSON, CSV, or Excel.
- Access them programmatically via the Apify API.

For more about datasets and exports, see Apify documentation:  
[https://docs.apify.com/platform/storage/dataset](https://docs.apify.com/platform/storage/dataset)

---

## ❤️ Made with Apify

Transform your hotel search automation with the most reliable and feature‑rich Google Hotels scraper on Apify.  

[**Made with ❤️**](https://apify.com/johnvc?fpr=9n7kx3)

Last Updated: 2025.11.26

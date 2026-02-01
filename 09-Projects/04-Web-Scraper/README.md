# Web Scraper

Extract data from websites using Python.

## Features

- Fetch webpage content with `requests`
- Parse HTML with `BeautifulSoup`
- Extract structured data
- Save to CSV

## Installation

```bash
pip install requests beautifulsoup4
```

## How to Run

```bash
python scraper.py
```

## What It Does

1. Fetches a webpage
2. Parses the HTML content
3. Extracts quotes and authors
4. Saves data to `quotes.csv`

## Example Output

```
==================================================
WEB SCRAPER DEMO
==================================================

Fetching webpage...
✅ Successfully fetched webpage!

"The way to get started is to quit talking and begin doing." 
  -- Walt Disney

"Don't let yesterday take up too much of today."
  -- Will Rogers

...

✅ Saved 10 quotes to quotes.csv
```

## Important Notes

⚠️ **Web Scraping Ethics:**
- Always check `robots.txt`
- Review the website's Terms of Service
- Don't overload servers (add delays)
- Consider using APIs instead
- Respect copyright and data privacy

## Learning Concepts

- HTTP requests
- HTML parsing
- DOM traversal
- Data extraction
- File writing (CSV)

## Better Alternatives

Many websites offer APIs instead:
- Weather: OpenWeatherMap API
- News: NewsAPI
- Crypto: CoinGecko API
- Twitter: Twitter API

---

Scrape responsibly! 🤖

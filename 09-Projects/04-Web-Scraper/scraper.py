"""
WEB SCRAPER

Scrapes data from websites using BeautifulSoup and requests.

Features:
- Fetch webpage content
- Parse HTML
- Extract data
- Save to CSV

Note: Always check website's robots.txt and terms of service before scraping!
"""

import requests
from bs4 import BeautifulSoup
import csv

def scrape_quotes():
    """
    Scrape quotes from quotes.toscrape.com
    This is a website designed for practicing web scraping.
    """
    
    url = "http://quotes.toscrape.com/"
    
    try:
        print("Fetching webpage...")
        response = requests.get(url)
        
        if response.status_code == 200:
            print("✅ Successfully fetched webpage!")
            
            # Parse HTML
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find all quotes
            quotes_div = soup.find_all('div', class_='quote')
            
            quotes_list = []
            
            for quote_div in quotes_div:
                # Extract text
                text = quote_div.find('span', class_='text').get_text()
                
                # Extract author
                author = quote_div.find('small', class_='author').get_text()
                
                quotes_list.append({
                    'text': text,
                    'author': author
                })
                
                print(f"{text}")
                print(f"  -- {author}\n")
            
            # Save to CSV
            save_to_csv(quotes_list)
            
            return quotes_list
        
        else:
            print(f"❌ Error: Status code {response.status_code}")
    
    except Exception as e:
        print(f"❌ Error: {e}")

def save_to_csv(quotes, filename="quotes.csv"):
    """Save quotes to CSV file"""
    
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['text', 'author'])
            writer.writeheader()
            writer.writerows(quotes)
        
        print(f"✅ Saved {len(quotes)} quotes to {filename}")
    
    except Exception as e:
        print(f"❌ Error saving file: {e}")

def scrape_weather():
    """
    Example of scraping weather data
    Note: This is a demonstration. Real-world use requires handling dynamic content.
    """
    
    print("\nWeather Scraping Example (requires dynamic content handling)")
    print("For real applications, use weather APIs instead!")
    
    # Example of what you might do:
    # 1. Use Selenium for JavaScript-rendered content
    # 2. Use an API (OpenWeatherMap, WeatherAPI)

def main():
    """Main function"""
    
    print("="*50)
    print("WEB SCRAPER DEMO")
    print("="*50)
    print("\nNote: This scraper targets quotes.toscrape.com,")
    print("a website designed for practicing web scraping.")
    print("Always respect robots.txt and website ToS!\n")
    
    # Scrape quotes
    quotes = scrape_quotes()
    
    if quotes:
        print(f"\n✅ Successfully scraped {len(quotes)} quotes!")

if __name__ == "__main__":
    main()

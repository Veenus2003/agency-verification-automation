import requests
from bs4 import BeautifulSoup

def get_website_text(url):
    """Fetches and extracts text content from the given URL."""
    try:
        headers = {"User-Agent": "Mozilla/5.0"}  # Avoid blocking
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise error for bad responses
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Extract text from paragraphs, headings, and metadata
        text = ' '.join([p.get_text() for p in soup.find_all(['p', 'h1', 'h2', 'h3'])])
        
        return text.strip()
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

# Test multiple agency websites
if __name__ == "__main__":
    agency_websites = [
        "https://www.digitalsilk.com/",
        "https://www.baunfire.com/",
        "https://fourbynorth.com/"
    ]

    for site in agency_websites:
        print(f"\nScraping: {site}")
        website_text = get_website_text(site)
        if website_text:
            print(f"Extracted {len(website_text)} characters of text.\n")
            print(website_text[:1000])  # Print only first 1000 characters

import requests
from bs4 import BeautifulSoup

def get_website_text(url):
    """Fetches and extracts text content from the given URL."""
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        text = ' '.join([p.get_text() for p in soup.find_all(['p', 'h1', 'h2', 'h3'])])

        return text.strip()
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

if __name__ == "__main__":
    agency_url = input("Enter the agency website URL: ").strip()
    
    print(f"\nScraping: {agency_url}")
    website_text = get_website_text(agency_url)
    
    if website_text:
        print(f"Extracted {len(website_text)} characters of text.\n")
        print(website_text[:1000])  # Print only the first 1000 characters

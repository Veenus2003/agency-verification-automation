import requests
from bs4 import BeautifulSoup
from verifier import check_agency_keywords
from store_results import save_result  # Import result storage function

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
        
        # Check for keywords to determine approval or rejection
        is_agency, found_keywords = check_agency_keywords(website_text)
        
        if is_agency:
            decision = "Approved"
            print(f"✅ Approved (Keywords found: {found_keywords})")
        else:
            decision = "Rejected"
            print("❌ Rejected (No relevant keywords found)")

        # Save decision in CSV file
        save_result(agency_url, decision, found_keywords)

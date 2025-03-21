import requests
from bs4 import BeautifulSoup
from verifier import check_agency_keywords
from ai_verifier import analyze_with_ai  # Import AI verification
from store_results import save_result

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
        
        # Step 1: Check keywords
        is_agency, found_keywords = check_agency_keywords(website_text)
        
        # Step 2: Use AI if no keywords found
        if is_agency:
            decision = "Approved"
            print(f"✅ Approved (Keywords found: {found_keywords})")
        else:
            print("🤖 No keywords found, asking AI for decision...")
            decision = analyze_with_ai(website_text)
            print(f"🤖 AI Decision: {decision}")

        # Save decision in CSV file
        save_result(agency_url, decision, found_keywords if is_agency else ["AI-based analysis"])

import requests
import re
from bs4 import BeautifulSoup
from verifier import check_agency_keywords  # Keyword-based verification
from ai_verify import analyze_with_ai  # AI verification
from store_results import save_result

def get_website_text(url):
    
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        text_blocks = soup.find_all(['p', 'h1', 'h2', 'h3', 'article',])

        # Extract text while removing unnecessary elements
        text = ' '.join([block.get_text() for block in text_blocks])
        filtered_text = re.sub(r'\b(Company|Contact|Careers|Privacy Policy|Linkedin|Twitter|Instagram|Dribbble)\b', '', text)

        if len(filtered_text) < 1000:
            more_text = ' '.join([p.get_text() for p in soup.find_all(['li', 'section'])])
            filtered_text += " " + more_text  

        return filtered_text.strip()

    except requests.exceptions.RequestException as e:
        print(f" Error fetching {url}: {e}")
        return None

if __name__ == "__main__":
    agency_url = input("Enter the agency website URL: ").strip()
    
    print(f"\nScraping: {agency_url}")
    website_text = get_website_text(agency_url)
    
    if website_text:
        print(f" Extracted {len(website_text)} characters of text.\n")
        #print(website_text);
        
        is_agency, found_keywords = check_agency_keywords(website_text)

        if is_agency:
            decision = "Approved"
            print(f"Approved (Keywords found: {found_keywords})")
        else:
            print("No keywords found, asking AI for decision...")
            decision = analyze_with_ai(website_text)  # Direct AI response

            
            if decision not in ["Approved", "Rejected"]:
                print(" AI Response Error: Unexpected output, forcing rejection.")
                decision = "Rejected"

        print(f"Final Decision: {decision}")

        
        if not found_keywords and decision == "Approved":
            print("No keywords found, but AI is confident. Keeping AI decision.")

        save_result(agency_url, decision, found_keywords if found_keywords else ["AI-based analysis"])

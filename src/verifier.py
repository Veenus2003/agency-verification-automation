import re

# List of agency-related keywords
AGENCY_KEYWORDS = [
    "services", "web design", "web development", "SEO agency", 
    "ads agency", "digital marketing", "marketing agency", "branding", "website creation"
]

def check_agency_keywords(text):
    """Checks if the given text contains any agency-related keywords."""
    text = text.lower()  # Convert to lowercase for case-insensitive search
    found_keywords = [kw for kw in AGENCY_KEYWORDS if re.search(rf"\b{kw}\b", text)]
    
    if found_keywords:
        return True, found_keywords  # Approved (Agency)
    return False, []  # Rejected (Not an Agency)

# Example usage
if __name__ == "__main__":
    sample_text = """
        We are a digital marketing and web design agency focused on building high-performance websites.
    """
    is_agency, keywords = check_agency_keywords(sample_text)
    
    if is_agency:
        print(f"✅ Approved (Keywords found: {keywords})")
    else:
        print("❌ Rejected (No relevant keywords found)")

import re


AGENCY_KEYWORDS = [
    "services", "web design", "web development", "SEO agency",
    "ads agency", "digital marketing agency", "agency", "website creation"
]

def check_agency_keywords(text):
    """Checks if the given text contains any agency-related keywords."""
    text = text.lower()  # Convert to lowercase for case-insensitive search
    found_keywords = [kw for kw in AGENCY_KEYWORDS if re.search(rf"\b{kw}\b", text)]

    if found_keywords:
        return True, found_keywords  
    return False, []  

# Example test
if __name__ == "__main__":
    sample_text = "We are a digital marketing and web design agency helping businesses grow."
    decision, keywords = check_agency_keywords(sample_text)
    print(f"Decision: {'Approved' if decision else 'Rejected'} (Keywords: {keywords})")

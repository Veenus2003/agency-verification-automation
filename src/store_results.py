import csv
import os

CSV_FILE = "agency_verification_results.csv"

def save_result(agency_url, decision, found_keywords):
    """Saves the verification result (Approved/Rejected) into a CSV file."""
    file_exists = os.path.isfile(CSV_FILE)
    
    with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        
        # Write header only if the file is new
        if not file_exists:
            writer.writerow(["Agency URL", "Decision", "Keywords Found"])
        
        writer.writerow([agency_url, decision, ", ".join(found_keywords)])

    print(f"✅ Decision saved in {CSV_FILE}")

# Example usage
if __name__ == "__main__":
    save_result("https://www.digitalsilk.com", "Approved", ["web design", "digital marketing"])

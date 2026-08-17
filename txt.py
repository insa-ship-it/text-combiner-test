import requests
from datetime import datetime

# ===== CONFIGURATION =====
# Add your list of TXT file URLs here
TXT_FILES = [
    "https://github.com/insa-ship-it/text-combiner-test/raw/refs/heads/main/Combos/013tv.com_8080.txt",
    "https://github.com/insa-ship-it/text-combiner-test/raw/refs/heads/main/Combos/0nmlause74.the-ninna.co.txt", 
    "https://github.com/insa-ship-it/text-combiner-test/raw/refs/heads/main/Combos/103.240.150.229_80.txt",
    "https://github.com/insa-ship-it/text-combiner-test/raw/refs/heads/main/Combos/138.199.41.89_22161.txt",
    "https://github.com/insa-ship-it/text-combiner-test/raw/refs/heads/main/Combos/143.244.35.74_80.txt",
    "https://github.com/insa-ship-it/text-combiner-test/raw/refs/heads/main/Combos/173.233.74.190_25461.txt",
    "https://github.com/insa-ship-it/text-combiner-test/raw/refs/heads/main/Combos/206.212.242.25_80.txt",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
]

# Output file
OUTPUT_FILE = "combined_list.txt"

# ===== FUNCTIONS =====
def fetch_txt_content(url):
    """Fetch content from a raw text URL"""
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        # Returns a list of lines, stripping whitespace
        return [line.strip() for line in response.text.splitlines() if line.strip()]
    except Exception as e:
        print(f"❌ Failed to fetch {url}: {e}")
        return []

def main():
    """Main function to combine text files"""
    print(f"🚀 Starting to combine {len(TXT_FILES)} text files...")
    
    all_lines = []
    
    # Process each URL
    for url in TXT_FILES:
        print(f"🔄 Processing: {url}")
        content = fetch_txt_content(url)
        if content:
            all_lines.extend(content)
            print(f"✅ Added {len(content)} lines from {url.split('/')[-1]}")
    
    # Remove duplicates while maintaining order
    unique_lines = list(dict.fromkeys(all_lines))
    
    # Write to output file
    with open(OUTPUT_FILE, "w", encoding="utf-8") as outfile:
        outfile.write(f"# Generated on {datetime.utcnow().isoformat()} UTC\n")
        outfile.write(f"# Total unique lines: {len(unique_lines)}\n\n")
        outfile.write("\n".join(unique_lines))
    
    print(f"\n🎉 Success! Combined content saved as '{OUTPUT_FILE}'")
    print(f"📄 Total lines: {len(unique_lines)}")

if __name__ == "__main__":
    main()

import requests
from datetime import datetime

# ===== CONFIGURATION =====
# Add your list of TXT file URLs here
TXT_FILES = [
    "https://github.com/insa-ship-it/text-combiner-test/raw/refs/heads/main/Combos/23.227.132.58_25461.txt",
    "https://github.com/insa-ship-it/text-combiner-test/raw/refs/heads/main/Combos/51.81.106.100_25461.txt", 
    "https://github.com/insa-ship-it/text-combiner-test/raw/refs/heads/main/Combos/81.31.194.66_8880.txt",
    "https://github.com/insa-ship-it/text-combiner-test/raw/refs/heads/main/Combos/Http___0g7hljf4wx.sasa24.xyz_80.txt",
    "https://github.com/insa-ship-it/text-combiner-test/raw/refs/heads/main/Combos/ahhshitherewegoagain.sytes.net_2096.txt",
    "https://github.com/insa-ship-it/text-combiner-test/raw/refs/heads/main/Combos/ak-47scan.dyndns.tv_25461.txt",
    "https://github.com/insa-ship-it/text-combiner-test/raw/refs/heads/main/Combos/altontestruzlegustaelnepe.neorpahe.top_8080.txt",
    "https://github.com/insa-ship-it/text-combiner-test/raw/refs/heads/main/Combos/ayudaavenezuela.hnsefpop.top_8080.txt",
    "https://github.com/insa-ship-it/text-combiner-test/raw/refs/heads/main/Combos/budgettvnow.com_83.txt",
    "https://github.com/insa-ship-it/text-combiner-test/raw/refs/heads/main/Combos/cemse.pw_57050.txt",
    "https://github.com/insa-ship-it/text-combiner-test/raw/refs/heads/main/Combos/colombiaplay.online_8080__panel.txt",
    "https://github.com/insa-ship-it/text-combiner-test/raw/refs/heads/main/Combos/hushaxx.net_80.txt",
    "https://github.com/insa-ship-it/text-combiner-test/raw/refs/heads/main/Combos/lunar.pm_8080.txt",
    "https://github.com/insa-ship-it/text-combiner-test/raw/refs/heads/main/Combos/neosfpoo.top_8080.txt",
    "https://github.com/insa-ship-it/text-combiner-test/raw/refs/heads/main/Combos/nocable.cc_8080.txt",
    "https://github.com/insa-ship-it/text-combiner-test/raw/refs/heads/main/Combos/tv.startseven.tn_2052.txt",
    "https://github.com/insa-ship-it/text-combiner-test/raw/refs/heads/main/Combos/uk-media.live_8880_.txt",
    "https://github.com/insa-ship-it/text-combiner-test/raw/refs/heads/main/Combos/wickediptv.live_8080.txt",
    "https://github.com/insa-ship-it/text-combiner-test/raw/refs/heads/main/Combos/wisz.online.txt",
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

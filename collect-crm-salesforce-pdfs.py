import os
import requests
from googlesearch import search
from urllib.parse import urlparse
from time import sleep

# Search queries
queries = [
    "CRM filetype:pdf",
    "Salesforce development filetype:pdf",
    "Salesforce tutorial filetype:pdf"
]

# Folder to save PDFs
output_dir = "downloaded_pdfs"
os.makedirs(output_dir, exist_ok=True)

# Max results per query
MAX_RESULTS = 10

# Download timeout (seconds)
TIMEOUT = 15

def sanitize_filename(url):
    return os.path.basename(urlparse(url).path).split("?")[0] or "downloaded.pdf"

def download_pdf(url, dest_folder):
    try:
        filename = sanitize_filename(url)
        filepath = os.path.join(dest_folder, filename)

        if not filename.endswith(".pdf"):
            print(f"❌ Skipping non-PDF: {url}")
            return

        print(f"⬇️ Downloading: {url}")
        response = requests.get(url, timeout=TIMEOUT)
        response.raise_for_status()

        with open(filepath, "wb") as f:
            f.write(response.content)
        print(f"✅ Saved to {filepath}")
    except Exception as e:
        print(f"⚠️ Error downloading {url}: {e}")

def collect_pdfs():
    for query in queries:
        print(f"\n🔍 Searching: {query}")
        results = search(query, num_results=MAX_RESULTS)
        for url in results:
            if url.lower().endswith(".pdf"):
                download_pdf(url, output_dir)
                sleep(1)  # Be polite to servers
            else:
                print(f"⚠️ Skipping non-PDF URL: {url}")

if __name__ == "__main__":
    collect_pdfs()

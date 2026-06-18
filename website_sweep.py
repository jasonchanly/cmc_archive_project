import os
import argparse
from pathlib import Path
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time

FILE_EXTENSIONS = (".pdf", ".doc", ".docx")


def sweep_url(url, save_dir):
    missing_progs = []
    # Fetch the page
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # Find all <a> links
    links = soup.find_all("a")

    for link in links:
        href = link.get("href")
        if not href:
            continue

        # Only download doc / pdf files
        if href.lower().endswith(FILE_EXTENSIONS):
            file_url = urljoin(url, href)
            filename = os.path.join(save_dir, os.path.basename(href))

            if Path(filename).exists():
                print(f"File already saved: {file_url}")
                continue
            else:
                print(f"Downloading: {file_url}")
            # Stream download
                try:
                    with requests.get(file_url, stream=True) as r:
                        r.raise_for_status()
                        with open(filename, "wb") as f:
                            for chunk in r.iter_content(chunk_size=8192):
                                f.write(chunk)

                except: # accept that there might be different errors regardless
                    print(f"Problem with file - not downloaded: {file_url}")
                    missing_progs.append(href.split("/")[-1])
                    continue

        elif any([x in href.lower() for x in ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]]):
            # these appear to be programmes but are unavailable on site
            missing_progs.append(href.split("/")[-1])

        time.sleep(1)

    return missing_progs


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--urls_fpath", type=str, help=".txt listing the URLs to be processed", default="archive_urls.txt")
    parser.add_argument("--save_dir", type=str, default="archives_dl_from_website")
    args = parser.parse_args()

    today = datetime.now().strftime("%Y-%m-%d")

    save_dir = Path(args.save_dir) / today
    save_dir.mkdir(exist_ok=True)
    missing_progs_fpath = save_dir.parent / f"{today}-dl-missing_progs.txt"
    all_missing_progs = []

    with open(args.urls_fpath) as f:
        archive_urls = [line.strip() for line in f.readlines() if line.strip()]

    print("Initialising sweep...")
    for link in archive_urls:
        all_missing_progs.extend(sweep_url(link, save_dir))
        with open(missing_progs_fpath, "a") as f:
            while all_missing_progs:
                f.write(all_missing_progs.pop(0) + "\n")

    print("Sweep complete")

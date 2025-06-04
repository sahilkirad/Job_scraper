# run.py
import os
import logging
from weworkremotely_scraper import WeWorkRemotelyScraper

def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def main():
    setup_logger()

    logging.info("==== US Job Scraper: WeWorkRemotely Edition ====")

    base_url = "https://weworkremotely.com"
    logging.info(f"[*] Target URL set to: {base_url}")

    # Ask user for keyword input
    keyword_input = input("Enter job title keywords (comma-separated, e.g., engineer,software,remote) - Leave empty for all jobs:\n")
    keywords = [kw.strip() for kw in keyword_input.split(",")] if keyword_input.strip() else []

    scraper = WeWorkRemotelyScraper(base_url=base_url, keywords=keywords)
    jobs = scraper.scrape_jobs()

    if jobs:
        logging.info(f"[+] Found {len(jobs)} jobs matching criteria.")
        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)

        # Ask user for output format
        output_format = input("Choose output format (csv or json): ").strip().lower()
        if output_format not in ['csv', 'json']:
            logging.warning("[!] Invalid format selected. Defaulting to JSON.")
            output_format = 'json'

        if output_format == 'json':
            json_path = os.path.join(output_dir, "weworkremotely_jobs.json")
            scraper.save_to_json(json_path)
            logging.info(f"[+] Results saved to {json_path}")
        else:  # csv
            csv_path = os.path.join(output_dir, "weworkremotely_jobs.csv")
            scraper.save_to_csv(csv_path)
            logging.info(f"[+] Results saved to {csv_path}")
    else:
        logging.warning("[!] No jobs found with given keywords.")

if __name__ == "__main__":
    main()
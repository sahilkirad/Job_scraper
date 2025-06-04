import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
from urllib.parse import urljoin
from save_utils import save_to_csv, save_to_json

class WeWorkRemotelyScraper:
    def __init__(self, base_url, keywords=None):
        self.base_url = base_url
        self.keywords = [kw.lower() for kw in keywords] if keywords else []
        self.job_listings = []

    def scrape_jobs(self):
        logging.info("[*] Scraping WeWorkRemotely with Selenium...")

        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("window-size=1920,1080")
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")

        driver = webdriver.Chrome(options=options)

        try:
            driver.get(self.base_url)
            time.sleep(5)

            soup = BeautifulSoup(driver.page_source, 'html.parser')
            job_sections = soup.find_all('li', class_='feature')

            for job_element in job_sections:
                self._process_job_listing(job_element)

        except Exception as e:
            logging.error(f"[!] An error occurred while scraping with Selenium: {e}", exc_info=True)
        finally:
            driver.quit()

        return self.job_listings

    def _process_job_listing(self, job_element):
        try:
            title_tag = job_element.find('h4', class_='new-listing__header__title')
            if not title_tag:
                return

            title = title_tag.get_text(strip=True)

            company_tag = job_element.find('span', class_='company') or job_element.find('div', class_='company')
            company = company_tag.get_text(strip=True) if company_tag else "N/A Company"

            location_tag = job_element.find('div', class_='region') or job_element.find('span', class_='region')
            location = location_tag.get_text(strip=True) if location_tag else "Remote"

            link_tag = job_element.find('a', href=True)
            if not link_tag:
                return

            full_url = urljoin(self.base_url, link_tag['href'])

            if not self.keywords or any(
                keyword in title.lower() or
                keyword in company.lower() or
                keyword in location.lower()
                for keyword in self.keywords
            ):
                job_data = {
                    'title': title,
                    'company': company,
                    'location': location,
                    'url': full_url,
                    'source': 'WeWorkRemotely'
                }
                if job_data not in self.job_listings:
                    self.job_listings.append(job_data)

        except Exception as e:
            logging.error(f"[!] Error processing job listing element: {e}", exc_info=True)

    def save_to_csv(self, filename):
        save_to_csv(self.job_listings, filename)

    def save_to_json(self, filename):
        save_to_json(self.job_listings, filename)
WeWorkRemotely Job Scraper 🚀
This is a Python-based job scraper designed to extract remote job listings from WeWorkRemotely.com. It allows users to search for jobs based on keywords and save the results in either CSV or JSON format.

Features ✨
Keyword Search: Filter job listings by specific keywords in the job title, company, or location. 🔎
Data Export: Save scraped job data to a CSV or JSON file. 💾
Headless Browse: Uses Selenium with headless Chrome to scrape data efficiently without opening a browser window. 🌐
Logging: Provides informative logs about the scraping process. 📜
Requirements 🛠️
Before running the scraper, ensure you have the following installed:

Python 3.x
pip (Python package installer)
Chrome browser (for ChromeDriver compatibility)
Installation 💻
Clone the repository:

Bash

git clone https://github.com/sahilkirad/Job_scraper_Project.git
cd weworkremotely-scraper

Install the required Python packages:

Bash

pip install selenium beautifulsoup4
Download ChromeDriver:
This scraper uses Selenium, which requires a WebDriver to interact with the Chrome browser. You need to download the appropriate ChromeDriver executable that matches your Chrome browser version.

Go to the ChromeDriver downloads page.
Find the version of ChromeDriver that corresponds to your installed Chrome browser version.
Download the zip file for your operating system.
Extract the chromedriver executable and place it in a directory that's in your system's PATH, or in the same directory as your run.py script.
Usage 🚀
Run the scraper:

Bash

python run.py
Follow the prompts:

You will be asked to Enter job title keywords (comma-separated, e.g., engineer,software,remote) - Leave empty for all jobs:
Enter your desired keywords separated by commas (e.g., python,developer,backend).
Press Enter without typing anything to scrape all available jobs.
Next, you will be prompted to Choose output format (csv or json):
Type csv to save the results in a CSV file.
Type json to save the results in a JSON file.
If you enter an invalid format, it will default to JSON.
View Results:
The scraped job data will be saved in an output directory created in the same location as your scripts.

output/weworkremotely_jobs.csv (if you chose CSV)
output/weworkremotely_jobs.json (if you chose JSON)
Project Structure 📁
run.py: The main script to execute the scraper. It handles user input and orchestrates the scraping and saving processes.
weworkremotely_scraper.py: Contains the WeWorkRemotelyScraper class, which handles the core scraping logic using Selenium and BeautifulSoup.
save_utils.py: Provides utility functions (save_to_csv, save_to_json) for saving the scraped data to different file formats.
Error Handling and Logging 🐞
The scraper includes basic error handling and logging.

Informative messages are printed to the console during execution.
Errors during scraping or job processing are logged, helping with debugging.
Contributing 🤝
Feel free to fork this repository, make improvements, and submit pull requests.

License 📄
This project is open-source and available under the MIT License.

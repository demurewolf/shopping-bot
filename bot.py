from selenium import webdriver
from selenium.webdriver.chrome.service import Service

CHROMEDRIVER_PATH = "/home/josiah/Documents/python/shopping-bot/chromedriver"
WEBSITES = ["amazon", "newegg", "microcenter", "bestbuy"]
URLS = list(map(lambda x: f"https://www.{x}.com", WEBSITES))
print(URLS)
print("Starting up shopping bot...")

# Straight from the Selenium 4.x docs
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
service = Service(executable_path=CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)

for url in URLS:
    driver.get(url)
    print(driver.title)

driver.close()

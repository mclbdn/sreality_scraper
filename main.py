from sreality import Sreality
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

sreality = Sreality(driver=driver, no_of_pages_to_scrape=3)

sreality.write_to_csv()

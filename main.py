from sreality import Sreality
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

sreality = Sreality(driver=driver, no_of_pages_to_scrape=3)

sreality.write_to_csv()

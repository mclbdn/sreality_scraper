from sreality import Sreality
from chart_maker import ChartMaker
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

print("####################################################################")
print("Hello and welcome to the Sreality scraper")
no_of_pages_to_scrape = input("How many pages do you wish to scrape? ")

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

sreality = Sreality(driver=driver, csv_name="properties", no_of_pages_to_scrape=3)
sreality.write_to_csv()

chart_maker = ChartMaker(csv_name=sreality.csv_name, num_of_pages=sreality.no_of_pages_to_scrape)
chart_maker.make_a_bar_chart()

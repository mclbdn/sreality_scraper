from sreality import Sreality
from chart_maker import ChartMaker
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

print("Hello and welcome to Sreality scraper")

while True:
    try:
        no_of_pages_to_scrape = int(input("How many pages do you wish to scrape? "))
    except ValueError:
        print("Please enter a number.")
    else:
        csv_name = str(input("Enter the name of a csv file to generate (i.e.'properties'): "))
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s)
        sreality = Sreality(driver=driver, csv_name=csv_name, no_of_pages_to_scrape=no_of_pages_to_scrape)
        break


generate_bar_chart_user_response = input("Do you wish to generate a bar chart of scraped data? If yes, type 'y', otherwise press and enter any other key to exit: ")

if generate_bar_chart_user_response.lower() == "y":
    chart_maker = ChartMaker(csv_name=sreality.csv_name, num_of_pages=sreality.no_of_pages_to_scrape)
    chart_maker.make_a_bar_chart()

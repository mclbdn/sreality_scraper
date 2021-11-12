from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import csv
from helper_functions import edit_text

URL = "https://www.sreality.cz/hledani/prodej/byty/praha?bez-aukce=1"
HEADER = ["no_of_rooms", "area", "locality", "price"]

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(URL)

with open('properties.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    writer.writerow(HEADER)

    properties = driver.find_elements(By.CLASS_NAME, "property")
    for property in properties:
        title = property.find_elements(By.CLASS_NAME, "name")[0]
        title_text = title.text
        no_of_rooms, area = edit_text(title_text)
        locality = property.find_elements(By.CLASS_NAME, 'locality')[0]
        locality_text = locality.text
        price = property.find_elements(By.CLASS_NAME, 'norm-price')[0]
        price_text = price.text
        print(no_of_rooms, area)
        writer.writerow([no_of_rooms, area, locality_text, price_text])


# properties = driver.find_elements(By.CLASS_NAME, "property")
# for property in properties:
#     title = property.find_elements(By.CLASS_NAME, "name")[0]
#     title_text = title.text
#     locality = property.find_elements(By.CLASS_NAME, 'locality')[0]
#     locality_text = locality.text
#     price = property.find_elements(By.CLASS_NAME, 'norm-price')[0]
#     price_text = price.text
#     print(f"{title_text} - {locality_text} - {price_text}")

driver.close()

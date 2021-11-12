from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import csv
from helper_functions import edit_text, get_prague_area
import time


URL = "https://www.sreality.cz/hledani/prodej/byty/praha?bez-aukce=1"
HEADER = ["no_of_rooms", "area_in_m2", "locality", "price"]

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(URL)

with open("properties.csv", "w", encoding="UTF8") as f:
    writer = csv.writer(f)

    writer.writerow(HEADER)

    i = 0

    while i <= 3:
        properties = driver.find_elements(By.CLASS_NAME, "property")
        for property in properties:
            title = property.find_elements(By.CLASS_NAME, "name")[0]
            title_text = title.text
            no_of_rooms, area = edit_text(title_text)
            locality = property.find_elements(By.CLASS_NAME, "locality")[0]
            locality_text = get_prague_area(locality.text)
            price = property.find_elements(By.CLASS_NAME, "norm-price")[0]
            price_text = price.text
            # If the owner didn't mention city part, skip
            if locality_text == None:
                continue
            writer.writerow([no_of_rooms, area, locality_text, price_text])

        next_btn = driver.find_element(By.CLASS_NAME, "paging-next")
        next_btn.click()
        time.sleep(10)
        i += 1

# driver.close()

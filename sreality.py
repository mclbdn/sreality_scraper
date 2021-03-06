import csv
import regex
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Sreality:
    def __init__(self, driver: WebDriver, csv_name: str, no_of_pages_to_scrape: int = 10000) -> None:
        self.URL = "https://www.sreality.cz/hledani/prodej/byty/praha?bez-aukce=1"
        self.CSV_HEADER = ["no_of_rooms", "area_in_m2", "locality", "price_in_kc"]
        self.driver = driver
        self.csv_name = csv_name
        self.no_of_pages_to_scrape = no_of_pages_to_scrape
        self.driver.get(self.URL)
        self.write_to_csv()

    # Replace text i.e. "Prodej bytu 3+1 94 m² (Podkrovní)" for a list of area & no_of_rooms
    def get_area_and_no_of_rooms(self, text: str):
        # Get rid of parenthesis
        sub = regex.sub(r"\([^)]*\)", "", text)
        # Split the text
        sub = sub.split()
        # Keep area in m2
        area = sub[-2] + sub[-1]
        # Get no. of rooms
        no_of_rooms = sub[-3]
        return [no_of_rooms, area]

    # Replace text i.e. "Neklanova, Praha 2 - Vyšehrad" for "Praha 2"
    def replace_prague_area(self, text: str):
        prague_areas = [
            "Praha 1",
            "Praha 2",
            "Praha 3",
            "Praha 4",
            "Praha 5",
            "Praha 6",
            "Praha 7",
            "Praha 8",
            "Praha 9",
            "Praha 10",
        ]

        for area in prague_areas:
            if area in text:
                return area

    def write_to_csv(self):
        with open(f"{self.csv_name}.csv", "w", encoding="UTF8") as f:
            writer = csv.writer(f)

            writer.writerow(self.CSV_HEADER)

            i = 0

            while i < self.no_of_pages_to_scrape:
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "property")))
                properties = self.driver.find_elements(By.CLASS_NAME, "property")
                for property in properties:
                    title = property.find_elements(By.CLASS_NAME, "name")[0]
                    title_text = title.text
                    no_of_rooms, area = self.get_area_and_no_of_rooms(title_text)
                    locality = property.find_elements(By.CLASS_NAME, "locality")[0]
                    locality_text = self.replace_prague_area(locality.text)
                    price = property.find_elements(By.CLASS_NAME, "norm-price")[0]
                    price_text = price.text
                    # If the owner didn't mention city part or price, skip
                    if locality_text == None or price_text == "Info o ceně u RK":
                        continue
                    price_text = price_text.replace(" ", "")
                    price_text = price_text.replace("Kč", "")
                    writer.writerow([no_of_rooms, area, locality_text, price_text])

                if i < self.no_of_pages_to_scrape:
                    next_btn = WebDriverWait(self.driver, 10).until(
                        EC.visibility_of_element_located((By.CLASS_NAME, "paging-next"))
                    )
                    next_btn.click()
                else:
                    return

                i += 1
            self.driver.quit()

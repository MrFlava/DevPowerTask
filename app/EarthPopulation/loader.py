import requests
from bs4 import BeautifulSoup

from .db import Session
from .models import Country
from .conf import WIKI_URL


class DataLoader:
    def __init__(self):
        self.session = Session()

    def get_data(self):
        response = requests.get(WIKI_URL)
        soup = BeautifulSoup(response.text, "html.parser")
        population_table = soup.find("table", {"class": "wikitable"})
        rows = population_table.find_all("tr")[1:]

        for row in rows:
            cols = row.find_all("td")
            if len(cols) < 5:
                continue

            country_name = cols[0].get_text(strip=True)
            pop_2023 = cols[2].get_text(strip=True).replace(",", "")
            region = cols[4].get_text(strip=True)

            if pop_2023.isdigit():
                c = Country(
                    name=country_name,
                    population=int(pop_2023),
                    region=region
                )
                self.session.merge(c)

            self.session.commit()

if __name__ == "__main__":
    DataLoader().get_data()
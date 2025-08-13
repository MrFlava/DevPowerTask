import requests
from bs4 import BeautifulSoup

from conf import WIKI_URL


class DataLoader:
    def __init__(self):
        pass

    def get_data(self):
        resp = requests.get(WIKI_URL)
        soup = BeautifulSoup(resp.text, "html.parser")
        table = soup.find("table", {"class": "wikitable"})
        rows = table.find_all("tr")[1:]

        for row in rows:
            cols = row.find_all("td")
            if len(cols) < 5:
                continue

            country_name = cols[0].get_text(strip=True)
            pop_2023 = cols[2].get_text(strip=True).replace(",", "")
            region = cols[4].get_text(strip=True)

            if pop_2023.isdigit():
                print(country_name, pop_2023, region)

if __name__ == "__main__":
    DataLoader().get_data()
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

        print(rows)

if __name__ == "__main__":
    DataLoader().get_data()
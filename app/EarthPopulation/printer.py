from sqlalchemy import text

from .db import Session

class Printer:
    def __init__(self):
        self.session = Session()

    def print_data(self):
        sql = text("""
        SELECT
          region,
          SUM(population) AS total_pop,
          (SELECT name FROM countries c2
             WHERE c2.region = c1.region
             ORDER BY population DESC
             LIMIT 1) AS largest_country,
          (SELECT population FROM countries c2
             WHERE c2.region = c1.region
             ORDER BY population DESC
             LIMIT 1) AS largest_pop,
          (SELECT name FROM countries c2
             WHERE c2.region = c1.region
             ORDER BY population ASC
             LIMIT 1) AS smallest_country,
          (SELECT population FROM countries c2
             WHERE c2.region = c1.region
             ORDER BY population ASC
             LIMIT 1) AS smallest_pop
        FROM countries c1
        GROUP BY region
        ORDER BY region;
        """)

        for row in self.session.execute(sql):
            print(f"Region: {row.region}")
            print(f"Total population: {row.total_pop}")
            print(f"Largest country: {row.largest_country}")
            print(f"Largest population: {row.largest_pop}")
            print(f"Smallest country: {row.smallest_country}")
            print(f"Smallest population: {row.smallest_pop}\n")

if __name__ == "__main__":
    Printer().print_data()
import csv

from src.types import Product

def extract() -> list[Product]:
    with open(
        "data/raw/products.csv",
          newline="", 
          encoding="utf-8"
          ) as file:
        products = csv.DictReader(file)

        result: list[Product] = []

        for product in products:
              result.append(
                  {
                    "id": product["id"],
                    "name": product["name"],
                    "category": product["category"],
                    "price": product["price"],
                    "supply": product["supply"],
                  }
              )

        return result
import csv

from src.exceptions import ExtractionError
from src.types import Product

FILE_PATH = "data/raw/products.csv"

REQUIRED_COLUMNS = {
  
  "id",
  "name",
  "category",
  "price",
  "supply",

}

def extract() -> list[Product]:
    try:
      with open(
            FILE_PATH,
            newline="", 
            encoding="utf-8"
            ) as file:
            reader = csv.DictReader(file)

            if reader.fieldnames is None:
              raise ExtractionError("The CSV file does not contain a header!")

            missing_columns = REQUIRED_COLUMNS - set(reader.fieldnames)

            if missing_columns:
                  raise ExtractionError(f"Missing required Columns {missing_columns}")

            products: list[Product] = []

            for row_number, product in enumerate(reader, start=2):
                try:
                  products.append(
                      {
                        "id": product["id"],
                        "name": product["name"],
                        "category": product["category"],
                        "price": product["price"],
                        "supply": product["supply"],
                      }
                  )
                except KeyError as exc:
                  raise ExtractionError(f"Invalid CSV structure at row {row_number}") from exc

            return products
    except FileNotFoundError as exc:
        raise ExtractionError(f"Input file not found: {FILE_PATH}") from exc
    except UnicodeDecodeError as exc:
        raise ExtractionError(f"Unable to decode input file: {FILE_PATH}") from exc
    except OSError as exc:
        raise ExtractionError(f"Unable to read input file: {FILE_PATH}") from exc
from src.extract import extract
from src.transform import transform


products = extract()

transformed_products = transform(products)

print(transformed_products)
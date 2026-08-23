from src.extract import extract
from src.transform import transform
from src.load import load

products = extract()

transformed_products = transform(products)

load(transformed_products)
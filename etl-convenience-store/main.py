from src.extract.csv import ExtractCsv
from src.extract.xlsx import ExtractXlsx
from src.transform import transform
from src.load import load

products = ExtractCsv()
transformed_products = transform(products)
load(transformed_products)

products_2 = ExtractXlsx()
transformed_products_2 = transform(products_2)
load(transformed_products_2)
from typing import TypedDict


class Product(TypedDict):
    id: str
    name: str
    category: str
    price: str
    supply: str


class TransformedProduct(TypedDict):
    id: str
    name: str
    category: str
    price: float
    supply: str
from src.types import Product, TransformedProduct


def transform(products: list[Product]) -> list[TransformedProduct]:
    result: list[TransformedProduct] = []

    for product in products:
        result.append(
            {
                "id": product["id"],
                "name": product["name"],
                "category": product["category"],
                "price": float(product["price"]),
                "supply": product["supply"],
            }
        )

    return result
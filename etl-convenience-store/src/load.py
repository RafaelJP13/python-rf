import os

import mysql.connector
from dotenv import load_dotenv

from src.types import TransformedProduct


load_dotenv()


def load(products: list[TransformedProduct]) -> None:
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
    )

    cursor = connection.cursor()

    for product in products:
        cursor.execute(
            """
            INSERT INTO products (name, category, price, supply)
            VALUES (%s, %s, %s, %s)
            """,
            (
                product["name"],
                product["category"],
                product["price"],
                product["supply"],
            ),
        )

    connection.commit()

    cursor.close()
    connection.close()
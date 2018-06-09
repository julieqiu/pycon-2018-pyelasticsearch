import json
import os

from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

from searchapp.models.products import Product

_all_products = None


def connect_to_db():
    engine = create_engine('postgresql+psycopg2://localhost/product_catalog', echo=True)
    return engine.connect()

def db_session():
    engine = create_engine('postgresql+psycopg2://localhost/product_catalog', echo=True)
    session = sessionmaker(bind=engine)
    return session()


def all_products_from_db():
    global _all_products

    if _all_products is None:
        _all_products = []

    with connect_to_db() as connection:
        result = connection.execute(
            """
            SELECT
                id
                , description
                , image_url
                , name
                , price
                , taxonomy
            FROM
                products
            """
        )
        for row in result:
            product_data = ProductData(id_, **product)
            _all_products.append(product_data)

    return _all_products


def write_products_json_to_db(filename: str=None):
    if not filename:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        filename = os.path.join(dir_path, 'products.json')

    products_to_write = []
    with open(filename) as product_file:
        for idx, product in enumerate(json.load(product_file)):
            id_ = idx + 1  # ES indexes must be positive integers, so add 1
            products_to_write.append(Product(id_, **product))

    with db_session() as session:
        for product in products_to_write:
            product = Product(
                name=product.name,
                taxonomy=product.taxonomy,
                image_url=product.image_url,
                description=product.description,
                price=product.price,
            )
            session.add(product)
        session.commit()


def create_products_table_db():
    with connect_to_db() as connection:
        connection.execute(
            """
            CREATE TABLE products (
                id INT PRIMARY KEY
                name VARCHAR NOT NULL
                description VARCHAR NOT NULL,
                image_url VARCHAR NOT NULL,
                taxonomy VARCHAR NOT NULL,
                price NUMERIC NOT NULL,
            );
            """
        )
        print('Created table!')

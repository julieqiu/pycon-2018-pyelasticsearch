import json
import os

from sqlalchemy.engine import create_engine

import textwrap
_all_products = None


class ProductData():
    """
    Our product records. In this case they come from a json file, but you could
    just as easily load them from a database, or anywhere else.
    """

    def __init__(self, id_, name, description, image, taxonomy, price):
        self.id = id_
        self.name = name
        self.description = description
        self.image = image
        self.taxonomy = taxonomy
        self.price = price

    def __str__(self):
        return textwrap.dedent("""\
            Id: {}
            Name: {}
            ImageUrl: {}
            Taxonomy: {}
            Price: ${}
            Description:

            {}
        """).format(self.id, self.name, self.image, self.taxonomy,
                    self.price, self.description)


def all_products(use_db_data=True):
    """
    Returns a list of ~20,000 ProductData objects, loaded from
    searchapp/products.json
    """
    if use_db_data:
        return all_products_from_db()

    global _all_products

    if _all_products is None:
        _all_products = []

        # Load the product json from the same directory as this file.
        dir_path = os.path.dirname(os.path.realpath(__file__))
        products_path = os.path.join(dir_path, 'products.json')
        with open(products_path) as product_file:
            for idx, product in enumerate(json.load(product_file)):
                id_ = idx + 1  # ES indexes must be positive integers, so add 1
                product_data = ProductData(id_, **product)
                _all_products.append(product_data)

    return _all_products


def connect_to_db():
    engine = create_engine('postgresql+psycopg2://localhost/product_catalog', echo=True)
    return engine.connect()


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
            products_to_write.append(ProductData(id_, **product))

    with connect_to_db() as connection:
        base_query = """
        INSERT INTO products (
            name
            , description
            , image
            , taxonomy
            , price
        ) VALUES
        """
        for product in products_to_write:

        ('B6717', 'Tampopo', 110, '1985-02-10', 'Comedy'),
        ('HG120', 'The Dinner Game', 140, DEFAULT, 'Comedy');


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

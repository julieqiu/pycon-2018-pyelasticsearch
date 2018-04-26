import json
import os
_all_products = None


def all_products():
    global _all_products
    id_ = 1
    if _all_products is None:
        _all_products = {}
        dir_path = os.path.dirname(os.path.realpath(__file__))
        products_path = os.path.join(dir_path, 'products.json')
        with open(products_path) as product_file:
            for idx, product in enumerate(json.load(product_file)):
                id_ = idx + 1  # ES ids have to be positive integers
                product['id'] = id_
                _all_products[id_] = product

    return _all_products

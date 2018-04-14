import json

_all_products = None


def all_products():
    global _all_products
    id_ = 1
    if _all_products is None:
        _all_products = {}
        with open('../../products.json') as product_file:
            print('loading!')
            for idx, product in enumerate(json.load(product_file)):
                id_ = idx + 1  # ES ids have to be positive integers
                product['id'] = id_
                _all_products[id_] = product

    return _all_products

import datetime
import json
from elasticsearch import Elasticsearch


def main():
    # by default we connect to localhost:9200
    es = Elasticsearch()

    # create an index in elasticsearch, ignore status code 400 (index already exists)
    es.indices.create(
        index='products',
        ignore=400,
    )

    products_data = json.load(open('products.json'))
    # datetimes will be serialized
    for i, product in enumerate(products_data):
        product_id = i + 1
        es.index(
            index='products',
            id=product_id,
            doc_type='products',
            body=product,
        )
        print(product_id, product['name'])

    # but not deserialized
    # products = es.get(index='products', doc_type='products')


if __name__ == '__main__':
    main()

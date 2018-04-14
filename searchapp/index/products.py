from elasticsearch import Elasticsearch

from searchapp.models.product import all_products

def main():
    # by default we connect to localhost:9200
    es = Elasticsearch()

    # create an index in ES, ignore status code 400 (index already exists)
    es.indices.create(
        index='products',
        ignore=400,
    )

    for i, product in all_products():
        es.index(
            index='products',
            id=product['id'],
            doc_type='products',
            body=product,
        )
        print(product['id'], product['name'])

    # but not deserialized
    # products = es.get(index='products', doc_type='products')


if __name__ == '__main__':
    main()

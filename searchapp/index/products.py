from elasticsearch import Elasticsearch

from searchapp.models.product import all_products

def main():
    # by default we connect to localhost:9200
    es = Elasticsearch()

    es.indices.delete(index='products', ignore=404)
    es.indices.create(
        index='products',
        body=dict({
            'mappings': {
                'products': {
                    'properties': {
                        'taxonomy': {
                            'type':  'keyword'
                        }
                    }
                }
            }
        })
    )

    for i, product in all_products().items():
        es.index(
            index='products',
            id=product['id'],
            body=product,
            doc_type='products',
        )
        print(product['id'], product['name'])

    # but not deserialized
    # products = es.get(index='products', doc_type='products')


if __name__ == '__main__':
    main()

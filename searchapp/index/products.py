from elasticsearch import Elasticsearch

from searchapp.models.product import all_products


def main():
    # by default we connect to localhost:9200
    es = Elasticsearch()

    es.indices.delete(index='products', ignore=404)
    es.indices.create(
        index='products',
        body=dict(
            mappings=dict(
                products=dict(
                    properties=dict(
                        taxonomy=dict(type='keyword'),
                        name=dict(
                            type='text',
                            analyzer='name_analyzer',
                        ),
                    )
                )
            ),
            settings=dict(
                analysis=dict(
                    analyzer=dict(
                        name_analyzer=dict(
                            type='standard',
                            stopwords=['made', 'of'],
                        ),
                    ),
                ),
            ),
        ),
    )

    for product in all_products().values():
        es.index(
            index='products',
            id=product['id'],
            body=product,
            doc_type='products',
        )
        print(product['id'], product['name'])


if __name__ == '__main__':
    main()

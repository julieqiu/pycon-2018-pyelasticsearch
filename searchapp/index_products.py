from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

from searchapp.utils import all_products


def products_to_index():
    for product in all_products().values():
        yield dict(
            _op_type='index',
            _index='products',
            _id=product['id'],
            _type='products',
            _source=dict(
                name=product['name'],
                image=product['image'],
                taxonomy=product['taxonomy'],
            ),
        )


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
                        name=dict(
                            type='text',
                            analyzer='name_analyzer',
                        ),
                    ),
                ),
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
        )
    )

    # print(product['id'], product['name'])
    bulk(es, products_to_index())

if __name__ == '__main__':
    main()

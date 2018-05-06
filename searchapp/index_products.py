from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

from searchapp.constants import DOC_TYPE, INDEX_NAME
from searchapp.data import all_products, ProductData


def products_to_index():
    for product in all_products():
        yield {
            '_op_type': 'index',
            '_index': INDEX_NAME,
            '_type': DOC_TYPE,
            '_id': product.id,
            '_source': {
                'name': product.name,
                'image': product.image,
            },
        }


def main():
    # Connect to localhost:9200 by default.
    es = Elasticsearch()

    es.indices.delete(index=INDEX_NAME, ignore=404)
    es.indices.create(
        index=INDEX_NAME,
        body={
            'mappings': {
                DOC_TYPE: {
                    'properties': {
                        'name': {
                            'type': 'text',
                            'fields': {
                                'english_analyzed': {
                                    'type': 'text',
                                    'analyzer': 'english',
                                }
                            }
                        }
                    }
                }
            },
            'settings': {},
        },
    )

    bulk(es, products_to_index())


def index_product(es, product: ProductData):
    """Add a single product to the ProductData index."""

    es.create(
        index=INDEX_NAME,
        doc_type=DOC_TYPE,
        id=product.id,
        body={
            "name": product.name,
            "image": product.image,
        }
    )
    print("Indexed {}".format(product.name))


if __name__ == '__main__':
    main()

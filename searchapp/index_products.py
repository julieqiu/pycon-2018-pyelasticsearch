from elasticsearch import Elasticsearch

from searchapp.constants import DOC_TYPE, INDEX_NAME
from searchapp.data import all_products, ProductData


def main():
    # Connect to localhost:9200 by default.
    es = Elasticsearch()

    es.indices.delete(index=INDEX_NAME, ignore=404)
    es.indices.create(
        index=INDEX_NAME,
        body={
            'mappings': {},
            'settings': {},
        },
    )

    index_product(es, all_products()[0])


def index_product(es, product: ProductData):
    """Add a single product to the ProductData index."""

    es.create(
        index=INDEX_NAME,
        doc_type=DOC_TYPE,
        id=1,
        body={
            "name": "A Great Product",
            "image": "http://placekitten.com/200/200",
        }
    )
    print("Indexed {}".format("A Great Product"))


if __name__ == '__main__':
    main()

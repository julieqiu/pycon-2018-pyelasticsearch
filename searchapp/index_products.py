from elasticsearch import Elasticsearch

from searchapp.constants import DOC_TYPE, INDEX_NAME
from searchapp.data import all_products, ProductData


def products_to_index():
    for product in all_products().values():
        yield dict(
            _op_type='index',
            _index=INDEX_NAME,
            _type=DOC_TYPE,
            _id=product['id'],
            _source=dict(
                name=product['name'],
                image=product['image'],
                taxonomy=product['taxonomy'],
            ),
        )


def main():
    # Connect to localhost:9200 by default.
    es = Elasticsearch()

    es.indices.delete(index=INDEX_NAME, ignore=404)
    es.indices.create(
        index=INDEX_NAME,
        body=dict(
            mappings=dict(),
            settings=dict(),
        )
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


if __name__ == '__main__':
    main()

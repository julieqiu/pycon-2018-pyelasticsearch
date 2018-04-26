from elasticsearch import Elasticsearch

from searchapp.utils import all_products


def main():
    # by default we connect to localhost:9200
    es = Elasticsearch()
    'men:clothing:outerwear:jackets'

    es.indices.delete(index='products', ignore=404)
    es.indices.create(
        index='products',
        body=dict(
            mappings=dict(
                products=dict(
                    properties=dict(
                        taxonomy=dict(type='keyword'),
                        taxonomy_analyzed=dict(
                            type='text',
                            analyzer='taxonomy_analyzer'
                        ),
                        name=dict(
                            type='text',
                            analyzer='name_analyzer',
                        ),
                    )
                )
            ),
            settings=dict(
                analysis=dict(
                    tokenizer=dict(
                        taxonomy_tokenizer=dict(
                            type='simple_pattern_split',
                            pattern='_',
                        ),
                    ),
                    analyzer=dict(
                        name_analyzer=dict(
                            type='standard',
                            stopwords=['made', 'of'],
                            ),
                        taxonomy_analyzer=dict(
                            tokenizer='taxonomy_tokenizer',
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
            body=dict(
                name=product['name'],
                description=product['description'],
                image=product['image'],
                taxonomy=product['taxonomy'],
                taxonomy_analyzed=product['taxonomy'],
            ),
            doc_type='products',
        )
        print(product['id'], product['name'])


if __name__ == '__main__':
    main()

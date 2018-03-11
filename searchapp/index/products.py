import datetime
from elasticsearch import Elasticsearch


def main():
    # by default we connect to localhost:9200
    es = Elasticsearch()

    # create an index in elasticsearch, ignore status code 400 (index already exists)
    es.indices.create(
        index='products',
        ignore=400,
    )

    orange_shirt = {
        'name': 'Orange Shirt',
        'description': 'This shirt is amazing and everybody loves it.',
        'image': 'https://wordans-mxelda46illwc0hq.netdna-ssl.com/files/model_specifications/2015/8/31/121007/121007_big.jpg?1441031839',
        'price': 10.00,
        'taxonomy': 'men:tops:shirts',
        'timestamp': datetime.datetime.now(),
    }

    other_orange_shirt = {
        'name': 'Other Orange Shirt',
        'description': 'Also an acceptable shirt.',
        'price': 15.00,
        'image': 'https://www.forever21.com/images/1_front_750/00252135-05.jpg',
        'taxonomy': 'men:tops:shirts',
        'timestamp': datetime.datetime.now(),
    }

    # datetimes will be serialized
    es.index(
        index='products',
        doc_type='products',
        id=42,
        body=orange_shirt,
    )
    es.index(
        index='products',
        doc_type='products',
        id=25,
        body=other_orange_shirt,
    )

    # but not deserialized
    import pdb; pdb.set_trace()
    products = es.get(index='products', doc_type='products')


if __name__ == '__main__':
    main()

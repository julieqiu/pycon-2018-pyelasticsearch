from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q


def search(term, count):
    client = Elasticsearch()
    client.transport.connection_pool.connection.headers.update({
        'content-type': 'application/json'
    })

    s = Search(using=client, index='products', doc_type='products')
    match_name = Q('match', name=dict(query=term, operator='and'))
    docs = s.query(match_name)[0:count].execute()

    return docs

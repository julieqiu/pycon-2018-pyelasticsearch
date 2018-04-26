from elasticsearch import Elasticsearch
from elasticsearch_dsl import A, Q, Search
from elasticsearch_dsl.aggs import Agg


DOC_TYPE = 'products'
INDEX_NAME = 'products'
HEADERS = {'content-type': 'application/json'}


def search(term: str, count: int) -> dict:
    client = Elasticsearch()
    client.transport.connection_pool.connection.headers.update(HEADERS)
    s = Search(using=client, index=INDEX_NAME, doc_type=DOC_TYPE)
    docs = s.query().execute()
    return docs

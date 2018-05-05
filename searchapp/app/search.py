from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from typing import List

from searchapp.constants import DOC_TYPE, INDEX_NAME

HEADERS = {'content-type': 'application/json'}


class SearchResult():
    """Represents a product returned from elasticsearch."""
    def __init__(self, id_, image, name):
        self.id = id_
        self.image = image
        self.name = name

    def from_doc(doc) -> 'SearchResult':
        return SearchResult(
                id_ = doc.meta.id,
                image = doc.image,
                name = doc.name,
            )


def search(term: str, count: int) -> List[SearchResult]:
    client = Elasticsearch()

    # Elasticsearch 6 requires the content-type header to be set, and this is
    # not included by default in the current version of elasticsearch-py
    client.transport.connection_pool.connection.headers.update(HEADERS)

    s = Search(using=client, index=INDEX_NAME, doc_type=DOC_TYPE)
    name_query = {'match_all': {}}
    docs = s.query(name_query)[:count].execute()


    return [SearchResult.from_doc(d) for d in docs]

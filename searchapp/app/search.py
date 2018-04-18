from elasticsearch import Elasticsearch
from elasticsearch_dsl import A, Q, Search
from elasticsearch_dsl.aggs import Agg


DOC_TYPE = 'products'
INDEX_NAME = 'products'
HEADERS = {'content-type': 'application/json'}

STOP_WORDS = {
    "a", "an", "and", "are", "as", "at", "be", "but", "by", "for", "if",
    "in", "into", "is", "it", "no", "not", "of", "on", "or", "such",
    "that", "the", "their", "then", "there", "these", "they", "this", "to",
    "was", "will", "with", "&", "", "-", "s"
}

REFINEMENTS = ['prices', 'taxonomy']


def search(term: str, count: int) -> dict:
    client = Elasticsearch()
    client.transport.connection_pool.connection.headers.update(HEADERS)
    s = Search(using=client, index=INDEX_NAME, doc_type=DOC_TYPE)

    match_name = Q('match', name=dict(query=term, operator='and'))
    docs = s.query(match_name)[0:count].execute()
    return docs

def aggregate():
    aggregations_query = Search(index=INDEX_NAME, doc_type='product')

    # The base query
    base_query = Search(index=INDEX_NAME, doc_type=DOC_TYPE)
    aggregations_query.query = base_query.query
#
    # copy the same query
    # aggregations_query = aggregations_query[0:0]  # size: 0 since we don't need hits
    # aggregations_query.fields([])

    aggregations = {
        'taxonomy': A('terms', field='taxonomy', size=2000),
    }

    for dim, agg in aggregations.items():
        filters = []
        refinements = {'taxonomoy': []}
        for refinements in [r for (dim, r) in refinements.items()]:
            for refinement in refinements:
                filters.append(refinement.query)
        refined_agg = A('filter', filter=(Q('bool', must=filters)), aggs={'taxonomy': agg})
        aggregations_query.aggs.bucket('taxonomy', refined_agg)

    # pylint: disable=no-member

    client = Elasticsearch()
    client.transport.connection_pool.connection.headers.update(HEADERS)
    aggregations_query_result = aggregations_query.using(client).execute()

    if not aggregations_query_result.success():
        raise Exception('aggregations query failed')
        return None

    return aggregations_query_result.aggregations.to_dict()

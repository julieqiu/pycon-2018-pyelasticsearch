from flask import render_template
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q
from app import app
import json


def search(term, count):
    client = Elasticsearch()
    client.transport.connection_pool.connection.headers.update({
        'content-type': 'application/json'
    })

    s = Search(using=client, index='products', doc_type='products')
    match_name = Q('match', name=dict(query=term, operator='and'))
    docs = s.query(match_name)[0:count].execute()

    return docs


@app.route('/')
@app.route('/index')
def index():
    terms = ['necklace', 'metal necklace', 'dress shirt', 'S.W. Basics',
             'SW Basics', 'jacket', 'blazer', 'basic', 'blue dress']

    products_by_category = {t: search(t, 9) for t in terms}

    return render_template(
        'index.html',
        title='PyCon 2018',
        products_by_category=products_by_category,
    )

_all_products = None


def all_products():
    global _all_products
    if _all_products is None:
        _all_products = {}
        with open('products.json') as product_file:
            for product in json.loads(product_file):
                _all_products[product['id']] = product

    return _all_products

@app.route('/search/<query>')
def search_single_product(query):
    products_by_category = {query: search(query, 9)}

    return render_template(
        'index.html',
        title='PyCon 2018',
        products_by_category=products_by_category,
    )

@app.route('/product/<id>')
def single_product(id_):
    product = json.dumps(all_products()[id_])

    return render_template(
        'product.html',
        title='PyCon 2018',
        product=product,
    )

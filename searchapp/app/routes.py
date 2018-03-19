from flask import render_template
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from app import app

def search(term):
    client = Elasticsearch()
    client.transport.connection_pool.connection.headers.update({'content-type':
        'application/json'})

    s = Search(using=client, index='products', doc_type='products')
    docs = s.query('term', name=term).execute()

    return docs


@app.route('/')
@app.route('/index')
def index():
    terms = [ 'Bonobos Pants', 'shirt', 'pants' , 'dress', 'jacket', 'a',
            'blazer']

    products_by_category = {t: search(t) for t in terms}

    return render_template(
        'index.html',
        title='PyCon 2018',
        products_by_category=products_by_category,
    )

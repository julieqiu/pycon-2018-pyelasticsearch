from elasticsearch import Elasticsearch
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Julie'}
    blue_dresses = [
        {
            'name': 'Blue Dress #1',
            'price': 100,
        },
        {
            'name': 'Blue Dress #2',
            'price': 200,
        },
    ]

    bonobos_pants = [
        {
            'name': 'Pants #1',
            'price': 300,
        },
        {
            'name': 'Pants #2',
            'price': 400,
        },
    ]

    es = Elasticsearch()
    orange_shirt_docs = es.search(
        index='products',
        doc_type='products'
    )['hits']['hits']

    orange_shirts = [doc['_source'] for doc in orange_shirt_docs]

    products_by_category = {
        'Blue Dress': blue_dresses,
        'Bonobos Pants': bonobos_pants,
        'Orange Shirts': orange_shirts,
    }

    return render_template(
        'index.html',
        title='PyCon 2018',
        user=user,
        products_by_category=products_by_category,
    )

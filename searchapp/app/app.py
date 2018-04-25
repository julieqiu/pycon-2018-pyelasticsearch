from flask import Flask, render_template, request

from searchapp.models.product import all_products
from searchapp.app.search import search, aggregate
import json

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    terms = ['necklace', 'metal necklace', 'necklce', 'brass necklace',
             'necklaces made of brass',
             'dress shirt', 'S.W. Basics', 'SW Basics', 'jacket',
             "Men's Jacket", 'wool jacket', 'blazer', 'basic', 'blue dress']

    products_by_category = {t: search(t, 9) for t in terms}

    return render_template(
        'index.html',
        title='PyCon 2018',
        products_by_category=products_by_category,
    )


@app.route('/search', methods=['GET', 'POST'])
def search_single_product():
    query = request.args.get('search')
    products_by_category = {query: search(query, 50)}

    return render_template(
        'index.html',
        title='PyCon 2018',
        products_by_category=products_by_category,
        search_term=query,
    )


@app.route('/product/<int:product_id>')
def single_product(product_id):
    product = json.dumps(all_products()[product_id], indent=4, sort_keys=True)

    return render_template(
        'product.html',
        title='PyCon 2018',
        product_json=product,
        search_term='',
    )

@app.route('/refinements')
def create_refinements():
    results = aggregate()
    taxonomies_and_counts = results['taxonomy']['buckets']


    return render_template(
        'refinements.html',
        refinements = results['taxonomy']['buckets'],
    )

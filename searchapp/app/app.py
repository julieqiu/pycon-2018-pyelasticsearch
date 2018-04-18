from flask import Flask, render_template, request

from searchapp.models.product import all_products
from searchapp.app.search import search, aggregate
import json

app = Flask(__name__)


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


@app.route('/search', methods=['GET', 'POST'])
def search_single_product():
    query = request.args.get('search')
    products_by_category = {query: search(query, 9)}

    return render_template(
        'index.html',
        title='PyCon 2018',
        products_by_category=products_by_category,
    )


@app.route('/product/<int:product_id>')
def single_product(product_id):
    product = json.dumps(all_products()[product_id], indent=4, sort_keys=True)

    return render_template(
        'product.html',
        title='PyCon 2018',
        product_json=product,
    )

@app.route('/refinements')
def refinements():
    aggregate()


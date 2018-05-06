from flask import Flask, render_template, request

from searchapp.data import all_products
from searchapp.app.search import search

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    """
    Search for products across a variety of terms, and show 9 results for each.
    """
    search_terms = [
        'necklace',
        'metal necklace',
        'necklce',
        'OK',
        'brass necklace',
        'a brass necklace',
        'necklaces made of brass',
        "men's jacket",
    ]

    num_results = 9
    products_by_category = [(t, search(t, num_results)) for t in search_terms]
    return render_template(
        'index.html',
        products_by_category=products_by_category,
    )


@app.route('/search', methods=['GET', 'POST'])
def search_single_product():
    """
    Execute a search for a specific search term.

    Return the top 50 results.
    """
    query = request.args.get('search')
    num_results = 50
    products_by_category = [(query, search(query, num_results))]
    return render_template(
        'index.html',
        products_by_category=products_by_category,
        search_term=query,
    )


@app.route('/product/<int:product_id>')
def single_product(product_id):
    """
    Display information about a specific product
    """

    product = str(all_products()[product_id - 1])

    return render_template(
        'product.html',
        product_json=product,
        search_term='',
    )

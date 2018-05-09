# Lesson 1: Indexing
We’ve provided a basic example of indexing data into elasticsearch to get you started. Step one is just running the indexer, and examining the results.

## Part 1: Starting the Flask App

### What you need to do:
1. Run `python searchapp/index_products.py`
2. Run `python searchapp/run.py`

### How you’ll know it worked:
1. http://localhost:9200/products_index/product/1 shows information about “A Great Product”.
2. http://localhost:9200/products_index shows information about the products index.
2. http://127.0.0.1:5000 returns “A Great Product” for every search term.


## Part 2: Indexing a Single Product
Now that we know that everything is working, it’s time to put real data in the index.

### What you need to do:
Modify the `index_product` function in `searchapp/index_product.py`.

The `product` object passed into `index_product` is currently not used for anything. Use it inside es.create.

### How you’ll know it worked:
Once you re-run index product, you’ll find that “A Great Product” has been replaced by “835 Mid-RIse Capri” everywhere.

### Helpful information
Open up `searchapp/index_products.py`. You’ll notice that `index_product` currently takes a `ProductData` object as an argument.

Currently, `index_product` does not use this argument. It creates a single product in the index using hardcoded data for `A Great Product` with the image of a kitten.

For this step, you’ll need to modify `index_product` to use the `ProductData` objected passed in.

#### Errors you might see:
<details>
<summary>elasticsearch.exceptions.ConflictError</summary>
When we create a document in elasticsearch, we must include a unique id. Are you passing the same id for every product in the es.create call? You should be passing `product.id`.
</details>

<details>
<summary>
ImportError: No module named searchapp.app.app
</summary>
Full Error Message:
```
Traceback (most recent call last):
  File "run.py", line 1, in <module>
    from searchapp.app.app import app
ImportError: No module named searchapp.app.app
```
All of our requirements were installed in a [virtual env](https://docs.python.org/3/library/venv.html). Is yours activated?

Run `source venv/bin/activate` from the root of the repository to activate the venv.
</details>

## Part 3: Indexing 20,000 more products
One product down, 19,999 to go.

### What you need to do:
Modify index_product to insert everything from `searchapp/products.json`, instead of just the first item.

### How you’ll know it worked:
http://127.0.0.1:5000 will now show nine products for every search result.

### Helpful information
All of the product data that we will be using in this workshop is stored in a json file, `searchapp/products.json`.

`searchapp/data.py` takes care of loading that json.

Take a look at `searchapp/data.py`. It defines a class, `ProductData` and a function, `all_products`.

`all_products` returns a list of `ProductData` objects created with the data in `searchapp/products.json`.

In this problem, you will need to modify `index_products` in `searchapp/index_products.py` to these products into your products index.

## Part 4: Bulk Indexing
We’re ready to start searching now! But let’s take a quick diversion to make indexing faster.

It takes about a minute to index 20,000 products. Inserting documents into elasticsearch one by one is slow. Fortunately, Elasticsearch has a bulk api, and elasticsearch-py provides a great wrapper around it.

### What you need to do:
Write a function called `products_to_index` to bulk index all the products.

### How you’ll know it worked:
When you run index_products.py should take only a few seconds to run, and http://127.0.0.1:5000 should continue to show nine results.


### Helpful information:
You’re going to invoke the `bulk` from `elasticsearch.helpers`, and pass it an iterable containing one insert action for each product. Your iterable can just be a list, or you can write a generator function and pass that to bulk.

Each action is a dictionary containing some special fields that start with underscores, and a `doc` field that contains the actual document to index.

You’ll want to:

1. Specify an `_op` type of index
2. Set `_index` and `_type` (doc type) to the appropriate constants
3. Provide the document (under the `_source` key), and `_id` just like in index_product


#### Where are the docs?
https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-bulk.html
http://elasticsearch-py.readthedocs.io/en/master/helpers.html

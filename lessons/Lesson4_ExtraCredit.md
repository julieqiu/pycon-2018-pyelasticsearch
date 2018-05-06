# Lesson 4: Extra Credit

Enough of necklaces, let’s buy a jacket.

There are plenty of jackets available in our data set, but only one shows up here.

The problem is that the words `men’s jacket` don’t usually show up in the product name, but they do show up in the product description. Let’s search the descriptions instead of the names.

Where are the docs?

There’s nothing new here, but you may want to review some of the documentation above.

## Part 1: Indexing Jackets (Indexing Product Description)

### What you need to do:
The indexing and search flow here is very similar to what you've seen before already. Just adapt them for product description!

In `searchapp/index_products.py`:

<details>
<summary>Hint: Step 1</summary>
Add the product description to the `_source` of your document.
</details>

<details>
<summary>Hint: Step 2</summary>
Add `description` to the mapping, and configure it to use our custom analyzer.
</details>

<details>
<summary>Hint: Step 3</summary>
Change `search.py` to reference `description.english_analyzed` instead of name.
</details>

<details>
<summary>Hint: Step 4</summary>
As usual, don’t forget to re-run `index_products` after changing it.
</details>

### How you’ll know it worked:
There are actually Jackets returned for the `men’s jackets` query.

This is a huge improvement for the jackets, but just about every other query has gotten worse. When there’s a match against the product name, the results are great, but we still need to support searches against the description. Fortunately, we can combine our name query and our description query, and search against both fields.

### Where are the docs?
https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-dis-max-query.html

## Part 2: Searching for Jackets (Dis Max Queries)

### What you need to do:
<details>
<summary>Hint</summary>
There are a few different ways to combine queries in elasticsearch, but `dis_max` is the best for this.

Separately create a `name_query` and `description_query`, and then combine them in the queries property of a `dis_max` query. Pass that dis_max query to `s.query`.

If the results don’t look much better, try adding `"tie_breaker": 0.7` to the dis_max query. This will boost items that match in both the name and description.
</details>

### How you’ll know it worked:
All of the results should look a bit better.

Play around with your query, and see how changes impact the results. Start off by adding `boost` properties to your name and description queries. Try swapping out the dis_max query for a bool query and playing with the boost values. Take your time, and try to really understand the impact each of your changes has. There’s always a way to make things a little better!

# Lesson 2: Searching
It’s time to return some real results!

Open up `searchapp/app/search.py`, and take a look at the `search` function. You’ll notice that it never makes use of the `term` that is passed in, and that’s why we get the same results for every query.


## A note on the hints below:
For each question below, we have provided hints in case you get stuck. Before looking that them, take some time to think through the question first!

When you want to read the spoilers, just click on them.

We recommend that you take your time, and to read the hints one at a time.

The more you try on your own, the more you’ll learn :)


## Part 1: Necklaces! (Term Query)
Let’s start by using a term query to search for products by their name.

### Where are the docs?
https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-term-query.html

### What you need to do:
Replace the match_all query with a term query. In the docs you’ll see "query" provided in the dictionary, but you don’t need to include that. Elasticsearch-dsl will automatically wrap the name_query for you.

### How you’ll know it worked:
Instead of seeing the same products for every query, you’ll see necklaces under the necklace query!

All of the other queries will return nothing.


## Part 2: Metal Necklaces (Match Query)
We made a search engine! But it’s not very good yet.

Let's take a look at the behavior of `term` queries by reading through [the term query docs](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-term-query.html) and playing around the [dev tools console](http://localhost:5601/app/kibana#/dev_tools/console).

Does it make sense why these return different results?

Note: you don't need `_source` in the queries belows, but it is handy for limiting the fileds returned by the search query for clarity. See [`_source` documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping-source-field.html).

```
POST _search
{
  "query": {
    "term" : { "name" : "necklace" }
  },
  "_source": ["name"]
}
```
```
POST _search
{
  "query": {
    "term" : { "name" : "Necklace" }
  },
  "_source": ["name"]
}
```
```
POST _search
{
  "query": {
    "term" : { "name" : "neklace" }
  },
  "_source": ["name"]
}
```

What happens when you run a [match query](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-match-query.html) instead?

Our next goal is to make the query for `Metal Necklace` work.

### What you need to do:
There are lots of products with metal and necklace in their name - return metal necklaces.

<details>
<summary>Hint</summary>
Replace your term query with a match query.
</details>

### How you’ll know it worked:
You’ll see results for a few more queries on http://127.0.0.1:5000. The metal necklaces will look really solid, with one exception: there will also be a metal filing cabinet included.

### Where are the docs?
https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-term-query.html
https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-match-query.html


## Part 3: Getting Rid of the Filing Cabinet
The results for `metal neklace` returned 8 metal necklaces and 1 filing cabinet.

Let’s deal with that filing cabinet.

Term was way too restrictive for our purposes, but the default behavior of match is a bit too permissive. Take another look at the match docs, and see if you can figure out how to make it match the eight metal necklaces, but not the filing cabinet.

### What you need to do:
What are some things that we do with a [match query](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-match-query.html)?

<details>
<summary>Hint</summary>
The critical section of the documentation is right at the top, under match.
Setting the operator flag to and will exclude the filing cabinet, without excluding any of our desired results.
The match query should contain a single key called “name,” the field your searching. The name key should map to a dictionary containing a query key, and the operator key.
</details>

### How you’ll know it worked:
The filing cabinet is gone! But everything else remains.

### Where are the docs?
https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-match-query.html


## Part 4: "Necklce"
There’s just one search term in our example that doesn’t have any results. “Necklce.” We could suggest that our customers check their spelling, but we don’t need to. Elasticsearch can provide good results even with minor misspellings.

### What you need to do:
<details>
<summary>Hint</summary>
The critical section of the documentation is Fuzziness.
You can add `{“fuzziness”: 2}` right next to the operator setting.
</details>

### How you’ll know it worked:
There are results for Necklce, that look just like the results for Necklace.

### Where are the docs?
https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-match-query.html

## Part 5: "OK"
How do your results for “OK” look? If you fixed the Necklce query the same way I did, you’re seeing results like “OV Kit” when searching for “OK.” If you did it a little differently, things might look fine. If your results still look good, try to figure out what I did. If they’re broken now, then how can we fix them without breaking Necklce?

## What you need to do:
<details>
<summary>Hint</summary>
The difference between seeing a bunch of OV Kit, and getting good results is caused by the value of the fuzziness key.
You’ve only got a few choices for the fuzziness value. Try it with 2 and try it with AUTO.
</details>

<details>
<summary>Hint</summary>
The critical section of the documentation is under [`AUTO`](https://www.elastic.co/guide/en/elasticsearch/reference/current/common-options.html#fuzziness
):
generates an edit distance based on the length of the term. Low and high distance arguments may be optionally provided AUTO:[low],[high], if not specified, the default values are 3 and 6, equivalent to AUTO:3,6 that make for lengths:
</details>


## How you’ll know it worked:
OK is back to normal, and necklce looks still works.

### Where are the docs?
https://www.elastic.co/guide/en/elasticsearch/reference/current/common-options.html#fuzziness

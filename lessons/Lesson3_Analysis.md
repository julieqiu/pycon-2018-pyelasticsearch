# Lesson 3: Analysis

For the next couple of queries, we’re going to be making changes to our index’s mapping and settings. We need to tell Elasticsearch more about the structure of our data, so it can effectively process our queries.

## Part 1: A Brass Necklace (Standard Analyzers)

The word `a` in `a brass necklace` is a *stop word*.

A *stop word* is a word that doesn’t add any extra information and can be ignored.

Elasticsearch comes with built in support for removing stop words. We just have to tell it that the `name` field of our products contains english text.

Once we do that, elasticsearch will filter out stop words in both the names of our products, and the search queries we run against them. I’ve left lots of spoilers visible below, because the documentation can easily lead you astray.

#### Disclaimer:
Unlike the previous problems, we are going to walk you through how to add stop words to your search app.

If you really want to work through this on your own, don’t read any further!

### What you need to do:
Head back to `index_products.py`. When you create the index, add a mapping that tells elasticsearch to analyze the `name` field as english.

Let's look at the mapping that we are going to index.
```
'mappings': {
    DOC_TYPE: {                                   # This mapping applies to products.
        'properties': {                             # Just a magic word.
            'name': {                                 # The field we want to configure.
                'type': 'text',                         # The kind of data we’re working with.
                'fields': {                             # create an analyzed field.
                    'english_analyzed': {                 # Name that field `name.english_analyzed`.
                        'type': 'text',                     # It’s also text.
                        'analyzer': 'english',              # And here’s the analyzer we want to use.
                    }
                }
            }
        }
    }
}
```
Now that we have the field (don’t forget to re-run the index script), we need to use it in our search.

Moving forward, simply swap in `name.english_analyzed` instead of `name` when writing search queries.

### How you’ll know it worked:
`A brass necklace` returns the same results as `brass necklace`.

### Where are the docs?
https://www.elastic.co/guide/en/elasticsearch/reference/current/analyzer.html
https://www.elastic.co/guide/en/elasticsearch/guide/current/using-stopwords.html
https://www.elastic.co/guide/en/elasticsearch/reference/6.2/analysis-lang-analyzer.html
https://www.elastic.co/guide/en/elasticsearch/reference/current/multi-fields.html

## Part 2: Necklace Made of Brass
The standard analyzers are powerful, but sometimes we need to augment them with information specific to our domain. We know that `made` doesn’t mean anything here, but elasticsearch doesn’t. So let’s create a custom analyzer that also includes `made` as a stop word.

### What you need to do:
Create the custom analyzer in the settings when you create the index. Like before, I think you’ll learn more from reading the code, than trying to write it from scratch.
```
'settings': {
    'analysis': {                                                 # magic word.
        'analyzer': {                                             # yet another magic word.
            'custom_english_analyzer': {              # The name of our analyzer.
                'type': 'english',                               # The built in analyzer we’re building on.
                'stopwords': ['made', '_english_'],   # Our custom stop words, plus the defaults.
            },
        },
    },
}
```

Re-run `index_products`, and it will create the analyzer. You can query it directly using the curl request below.

### How you’ll know it worked:
```
curl -X POST localhost:9200/products_index/_analyze -d '{"analyzer": "custom_english_analyzer", "text": "necklace made of brass"}' -H 'Content-Type: application/json'
```

Yields:
```
{
   "tokens":[
      {
         "token":"necklac",
         "start_offset":0,
         "end_offset":8,
         "type":"<ALPHANUM>",
         "position":0
      },
      {
         "token":"brass",
         "start_offset":17,
         "end_offset":22,
         "type":"<ALPHANUM>",
         "position":3
      }
   ]
}
```

### Where are the docs?
https://www.elastic.co/guide/en/elasticsearch/reference/current/analysis-stop-analyzer.html


## Part 3: Necklace Made of Brass (English Analyzer)
Note that `made` and `of` are both missing.

You can try the same query with the `english` analyzer directly, and you’ll see that `of` is removed, but `made` is not.

`Necklaces made of brass` still doesn’t return anything – we need to actually use our custom analyzer.

### What you need to do:
<details>
<summary>Hint</summary>
Swap out the english analyzer in the mapping, for the `custom_english_analyzer`.

As usual, don’t forget to re-run `index_products` after changing it.
</details>

### How you’ll know it worked:
We get some `necklaces made of brass`!

### Where are the docs?
https://www.elastic.co/guide/en/elasticsearch/reference/current/analyzer.html

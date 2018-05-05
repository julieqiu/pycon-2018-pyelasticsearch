# Hello! This is the Kibana Dev tools console, we'll use this to interact with Elasticsearch

#--------------------------------------
# Basic Search: Querying documents with GET
#--------------------------------------
# We now have about 20k products in the index!
# Find *all* documents

GET /products_index/products/_search


#__________________________________________________
# Let's find all necklaces!
GET /products/products/_search
{
  "query": {
    "match": {
      "name": "necklace"
    }
  }
}

# Results are ranked by "relevance" (_score)
# More info: https://www.elastic.co/guide/en/elasticsearch/guide/current/relevance-intro.html

# Let's look for all the brass necklaces.
# We'll use match_phrase since "brass necklace" is 2 words.
GET /products/products/_search
{
  "query": {
    "match_phrase": {
      "name": "brass necklace"
    }
  }
}


#__________________________________________________
# We can also do boolean combinations of querys
# Let's find all docs with "soup" and "san francisco" in the business name

GET /inspections/report/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "business_name": "soup"
          }
        },
        {
          "match_phrase": {
            "business_name": "san francisco"
          }
        }
      ]
    }
  }
}

#
# Or negate parts of a query, businesses without "soup" in the name (maybe you hate soup)

GET /inspections/report/_search
{
  "query": {
    "bool": {
      "must_not": [
        {
          "match": {
            "business_name": "soup"
          }
        }
      ]
    }
  }
}

#__________________________________________________
# Combinations can be boosted for different effects
# Let's emphasize places with "soup in the name"

GET /inspections/report/_search
{
  "query": {
    "bool": {
      "should": [
        {
          "match_phrase": {
            "business_name": {
              "query": "soup",
              "boost" : 3
            }
          }
        },
        {
          "match_phrase": {
            "business_name": {
              "query": "san francisco"
            }
          }
        }
      ]
    }
  }
}

# Sometimes it's unclear what actually matched.
# We can highlight the matching fragments:

GET /inspections/report/_search
{
  "query" : {
    "match": {
      "business_name": "soup"
    }
  },
  "highlight": {
    "fields": {
      "business_name": {}
    }
  }
}


#__________________________________________________
# Finally, we can perform filtering, when we don't need text analysis (or need to do exact matches, range queries, etc.)
# Let's find soup companies with a health score greater than 80

GET /inspections/report/_search
{
  "query": {
      "range": {
        "inspection_score": {
          "gte": 80
        }
      }
  },
  "sort": [
    { "inspection_score" : "desc" }
  ]
}

# More info: https://www.elastic.co/guide/en/elasticsearch/guide/current/structured-search.html

# We can also sort our results by "inspection_score"



# Aggregations (one use case is faceting data) are very interesting
# We won't have time to cover aggregation in depth now, but we want to get you familiar with
# how they work, so you can use them on your own

# Let's search for the term "soup", and bucket results by health score (similar to the facets you would see in an ebay site)
# Show: https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313.TR12.TRC2.A0.H0.Xwatch.TRS0&_nkw=watch&_sacat=0

GET /inspections/report/_search
{
  "query": {
    "match": {
      "business_name": "soup"
    }
  }
 ,"aggregations" : {
    "healthscore" : {
      "range" : {
        "field" : "healthscore",
        "ranges" : [
          {
            "key" : "0-80",
            "from" : 0,
            "to" : 80
          },
          {
            "key" : "81-90",
            "from" : 81,
            "to" : 90
          },
          {
            "key" : "91-100",
            "from" : 91,
            "to" : 100
          }
        ]
      }
    }
  }
}


# Geo search is another powerful tool for search
# Let's find soup restaurants closest to us!
# We have the geo point within the document, let's use it

GET /inspections/report/_search

# Let's execute the follow geo query, to sorted restaurants by distance by us

GET /inspections/report/_search
{
  "query": {
    "match": { "business_name": "soup"}
  },
  "sort": [
    {
      "_geo_distance": {
        "coordinates": {
          "lat":  37.800175,
          "lon": -122.409081
        },
        "order":         "asc",
        "unit":          "km",
        "distance_type": "plane"
      }
    }
    ]
}

# Error! Elasticsearch doesn't know the field is a geopoint
# We must define this field as a geo point using mappings
# Mapping are helpful for defining the structure of our document, and more efficiently storing/searching the data within our index
# We have numbers/dates/strings, and geopoints, let's see what elasticsearch thinks our mapping is

GET /inspections/_mapping/report

# Let's change the mapping, delete our index, and perform our bulk import again
# In production scenarios, you may prefer to use the reindex API, you can add new mapping fields without needing to migrate the data

DELETE inspections

PUT /inspections

PUT inspections/_mapping/report
{
"properties": {
          "business_address": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "business_city": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "business_id": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "business_latitude": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "coordinates": {
              "type": "geo_point"
          },
          "business_longitude": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "business_name": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "business_phone_number": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "business_postal_code": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "business_state": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "inspection_date": {
            "type": "date"
          },
          "inspection_id": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "inspection_score": {
            "type": "long"
          },
          "inspection_type": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "risk_category": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "violation_description": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "violation_id": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          }
        }
}


# Now we can execute our original geo query

GET /inspections/report/_search
{
  "query": {
    "match": { "business_name": "soup"}
  },
  "sort": [
    {
      "_geo_distance": {
        "business_location": {
          "lat":  37.800175,
          "lon": -122.409081
        },
        "order":         "asc",
        "unit":          "km",
        "distance_type": "plane"
      }
    }
    ]
}

# That was a very short introduction to geo queries and mappings, the goal was to get your feet wet to hopefuly go off and learn more


# Let's finish the CRUD components, we covered C, and R, let's show show to update and delete documents

# Let's add a flagged field to one of our documents, using a partial document update

GET /inspections/report/_search

POST /inspections/report/5/_update
{
   "doc" : {
      "flagged" : true,
      "views": 0
   }
}

# Documents are also versioned in Elasticsearch, if your application has the entire version, you can use another PUT command (notice how the version increments)

PUT /inspections/report/5
{
  "business_address": "2162 24th Ave",
  "business_city": "San Francisco",
  "business_id": "5794",
  "business_latitude": "37.747228",
  "business_location": {
    "type": "Point",
    "coordinates": [
      -122.481299,
      37.747228
    ]
  },
  "business_longitude": "-122.481299",
  "business_name": "LINCOLN HIGH SCHOOL",
  "business_phone_number": "+14155752700",
  "business_postal_code": "94116",
  "business_state": "CA",
  "inspection_date": "2016-09-07T00:00:00.000",
  "inspection_id": "5794_20160907",
  "inspection_score": "96",
  "inspection_type": "Routine - Unscheduled",
  "risk_category": "Low Risk",
  "violation_description": "Unapproved or unmaintained equipment or utensils",
  "violation_id": "5794_20160907_103144",
  "flagged": true,
  "views": 0
}

# To delete a document, we can just pass the document id to the DELETE API

DELETE /inspections/report/5

# That completed the CRUD section

# - Analyzers
# Text analysis is core to Elasticsearch, and very important to understand
# As you saw a mapping configuration for data types in the previous example, you can also configure an analyzer per field or an entire index!
# Analysis = tokenization + token filters

# Tokenization breaks sentences into discrete tokens

GET /test/_analyze
{
  "tokenizer": "standard",
  "text": "Brown fox brown dog"
}

# And filters manipulate those tokens

GET /test/_analyze
{
  "tokenizer": "standard",
  "filter": ["lowercase"],
  "text": "Brown fox brown dog"
}

# There is a wide variety of filters.

GET /test/_analyze
{
  "tokenizer": "standard",
  "filter": ["lowercase", "unique"],
  "text": "Brown brown brown fox brown dog"
}

# Did you notice the "Brown" vs "brown" ?



#__________________________________________________
# A tokenizer + 0 or more token filters == analyzer

# Let's go back to one of our examples, say we need to separate the tokens in
# the Soup-or-Salad restaurant name

POST _analyze
{
  "analyzer": "standard",
  "text": "soup.or.salad"
}

# The standard analyzer divides text into terms on word boundaries, as defined by the Unicode
# Text Segmentation algorithm. It removes most punctuation, lowercases terms, and supports removing stop words.
# But we aren't getting "soup" as a separate token

POST _analyze
{
  "analyzer": "simple",
  "text": "soup.or.salad"
}

# Now we have "soup" as a separate token and may want to use this analyzer in the future

#__________________________________________________
# Understanding analysis is very important, because
# the emitted tokens can change a lot!

GET /test/_analyze
{
  "tokenizer": "standard",
  "filter": ["lowercase"],
  "text": "THE quick.brown_FOx Jumped! $19.95 @ 3.0"
}

GET /test/_analyze
{
  "tokenizer": "letter",
  "filter": ["lowercase"],
  "text": "THE quick.brown_FOx Jumped! $19.95 @ 3.0"
}

# Another example with uax_url_email tokenizer

GET /test/_analyze
{
  "tokenizer": "standard",
  "text": "elastic@example.com website: https://www.elastic.co"
}

GET /test/_analyze
{
  "tokenizer": "uax_url_email",
  "text": "elastic@example.com website: https://www.elastic.co"
}


# More info: https://www.elastic.co/guide/en/elasticsearch/guide/current/_controlling_analysis.html

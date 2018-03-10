# pycon-2018-pyelasticsearch

## Tutorial Pre-Work
1. Clone this repository locally
2. Set up a virtualenv
```
virtualenv venv
source venv/bin/activate

# If you are using a Python 3 version, virtual environment support is included
# in it, so all you need to do to create one is this:
python3 -m venv venv
```
3. Install python 3.6.2 with pyenv
See instructions here: https://github.com/pyenv/pyenv
For OSX:
```
brew install pyenv
pyenv install 3.6.2
# Inside the root of the repository:
pyenv local 3.6.2
```
4. Install elasticsearch and sense

5. Install requirements (inside your virtualenv)
```
pip install -r requirements.txt
```


------------------------
TODO
1. Get JSON blobs of 250 products (variants)
- Name
- Description
- Price
- Brand Name
- Color (standard)
- Image url

2. Make a UI for search terms with Flask and Jinja and ability to type in a custom term
- Blue dress
- Blue dress shirt
- Pants that are leather
- Green pants
- Bonobos Pants

3. Get promo codes from Elastic + AWS

4. Exercise

5. Make Slides for Lecture
- What is Elasticsearch
- ES Terminology


Make sure the UI works
- Type in a search term


Things to search for:
1. Exact Substring: Name
- Exact text, Exact case,
2. TermQuery
3. MatchQuery
4. MatchAllQuery
5. DisMax Query: search for product name and description and weight the name more highly
Intro basic tools that kind of work but are terrible for various reasons
- Index with name, description and ID
- 1.5 Hours:
  - Make search work
  - Explore data with Sense
  - Intro matching: exact, fuzzy and dismax
- List of challenges:
1) here's a search term: 'blue dress' and example products in the dataset
-- typing in --> bad results
2) play with matchers --> try and get good results across those things
TODO: Answers ideas
- Hint 1: This is what an analzyer is
- Series of hints: analyzers might be useful, check out this description
-- Analyzers (remove stop words)
-- Tokenization
-- Boosting
-- Scoring
-- Preprocessing


PART II

Lecture: What is ES; Terminology, etc.

Advanced Queries
7. Index and Search Price
- Less than, greater than
- Uncomment thing in the UI --> price refinement
- Indexing price, reindexing
- Hard conditional with a search term

8. Index and Search Color

9. Clustering

10. Refinements and aggregations
- There are [Some] results...
- Color, Price and Brand
- Aggregation over all of the refinments

11. Writing to Elasticsearch
-- More effective to recreate a new index
-- Part III: Update API

12. Scalability: framing it as cool to understand, but not necessarily help you
- Why ES scales well
- https://www.elastic.co/guide/en/elasticsearch/guide/current/_add_failover.html

HOSTED Elasticsearch -- getting things up and running in production:
TODO: Julie to get promo codes for students
-- $$ for hosted elasticsearch exists
-- Contact at AWS for free promo codes

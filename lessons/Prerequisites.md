# Tutorial Pre-Work

In this tutorial, you will be building a search engine to search for product attributes using a Flask app and Elasticsearch.

To participate in this tutorial, you need to complete the following prerequisites:

1. Install [Python 3.6.4](https://www.python.org/downloads/release/python-364/).

2. Install Elasticsearch 6.2 and Kibana 6.2. (Note: You may need to install [Java](https://java.com/en/download/))

  - For OS X, you can use [Homebrew](https://brew.sh/):
```
brew update
brew install kibana
brew install elasticsearch

brew services start elasticsearch
brew services start kibana
```
  - For Windows or Linux, see the Elastic downloads page for[Elasticsearch](https://www.elastic.co/downloads/elasticsearch) and [Kibana](https://www.elastic.co/downloads/kibana).

  - Make sure you can visit http://localhost:5601/ and http://localhost:9200/ in your browser.

3. Clone the `pycon-2018-pyelasticsearch` repository to your computer by running:
```
git clone github.com/julieqiu/pycon-2018-pyelasticsearch
```

4. In root of the repository, set up a virtualenv:
```
python3 -m venv venv
source venv/bin/activate
```

5. Install the necessary python requirements:
```
pip install -r requirements.txt
```

6. Set up the searchapp:
```
pip install -e .
```

You're all set for the tutorial this Wednesday! :)

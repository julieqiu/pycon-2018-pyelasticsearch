# [Build a Search Engine with Python + Elasticsearch](https://us.pycon.org/2018/schedule/presentation/53/)

## Instructors
Julie Qiu
Jim Grandpre

## [Tutorial Presentation](https://docs.google.com/presentation/d/1le9vVCVb03AIPoWbsI4w__aop-3P9OEHVt56QJl6RnA/edit)

# Tutorial Pre-Work
In this tutorial, you will be building a search engine to search for product attributes using a Flask app and Elasticsearch.

To participate in this tutorial, you need to complete the following prerequisites:

1. Clone this repository to your computer by running:
```
cd $HOME
git clone github.com/julieqiu/pycon-2018-pyelasticsearch
```

2. Install the following:

- Python 3.6.4 (https://www.python.org/downloads/release/python-364/)
- Elasticsearch 6.2 and Kibana 6.2 (https://www.elastic.co/guide/en/elasticsearch/reference/6.2/install-elasticsearch.html)

- For OS X, you can use [Homebrew](https://brew.sh/):
```
brew update
brew install kibana
brew install elasticsearch
```

3. In this directory, set up a virtualenv
```
python3 -m venv venv
source venv/bin/activate
```

4. In this directory, install the necessary python requirements:
```
pip install -r requirements.txt
```
- Libraries you will be installing:
[elasticsearch-py](https://github.com/elastic/elasticsearch-py)
[Flask](http://flask.pocoo.org)

5. In this directory, set up the searchapp:
```
pip install -e .
```

6. Make sure these commands work:
```
brew services start elasticsearch
brew services start kibana

python searchapp/run.py
```


# Tutorial Pre-Work

1. Install Python 3.6.4

https://www.python.org/downloads/release/python-364/


2. Install elasticsearch and sense

OS X:
```
brew update
brew install elasticsearch
brew services start elasticsearch
```

3. Set up a virtualenv
```
python3 -m venv venv
source venv/bin/activate
```

4. Install packages elasticsearch-py and flask
```
pip install -r requirements.txt
```
elasticsearch-py: https://github.com/elastic/elasticsearch-py

5. Make sure these commands work:
```
flask run
python3 test_elasticsearch.py
```

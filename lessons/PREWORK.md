# Tutorial Pre-Work

1. Install Python 3.6.4

https://www.python.org/downloads/release/python-364/

2. Install elasticsearch

OS X:
```
brew update
brew install kibana
brew install elasticsearch
brew services start elasticsearch
```
3. Clone this repository in your home folder:

```
cd $HOME
git clone github.com/julieqiu/pycon-2018-pyelasticsearch
```

4. In this directory:
- Set up a virtualenv:
```
python3 -m venv venv
source venv/bin/activate
```
- Install the dependencies:
```
pip install -r requirements.txt
```
- Libraries you will be installing:
[elasticsearch-py](https://github.com/elastic/elasticsearch-py)
[Flask](http://flask.pocoo.org)

5. Set the FLASK_APP path
```
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
export FLASK_APP=${DIR}/searchapp/searchapp.py
```

6. Make sure these commands work:
```
flask run
python3 test_elasticsearch.py
```

7.
```

#!/usr/bin/env bash

source venv/bin/activate

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
export FLASK_APP=${DIR}/searchapp/searchapp.py
export FLASK_DEBUG=1

pip install -e .

brew services start elasticsearch
brew services start kibana
```

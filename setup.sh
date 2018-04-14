source venv/bin/activate

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
export FLASK_APP=${DIR}/searchapp/searchapp.py
export FLASK_DEBUG=1

pip install -e .

brew services start elasticsearch
brew services start kibana

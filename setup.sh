source venv/bin/activate

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
export FLASK_APP=${DIR}/searchapp/searchapp.py

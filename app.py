import sys
import glob
import os

# Automatically add virtualenv site-packages to sys.path so any python command works
base_dir = os.path.dirname(os.path.abspath(__file__))
patterns = [
    '/opt/render/project/**/site-packages',
    os.path.join(base_dir, '*venv*/**/site-packages'),
    os.path.join(base_dir, '../*venv*/**/site-packages'),
    os.path.expanduser('~/.local/**/site-packages'),
]
for pat in patterns:
    for p in glob.glob(pat, recursive=True):
        if p not in sys.path:
            sys.path.insert(0, p)

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return {
        'message': 'pssssss is running',
        'status': 'ok'
    }

@app.route('/health')
def health():
    return {'status': 'healthy'}, 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=False)

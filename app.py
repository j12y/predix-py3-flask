
import os
import sys

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return sys.version

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=True)

import os

from flask import Flask, render_template
from gevent.pywsgi import WSGIServer
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.jinja')

if __name__ == '__main__':
    wsgi = WSGIServer(('0.0.0.0', int(os.environ.get('PORT'))), app)
    wsgi.serve_forever()

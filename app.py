import os
from datetime import datetime

from flask import Flask, render_template, request, abort
from gevent.pywsgi import WSGIServer
from dotenv import load_dotenv

load_dotenv()

import source.db as db
from source.tier import tier_datetime

app = Flask(__name__)
app.jinja_env.globals.update(tier_datetime=tier_datetime)

@app.route('/')
def index():
    tiers = db.all_tiers()
    return render_template('index.jinja', tiers=tiers)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('create.jinja')
    tier = request.get_json()
    if not all(tier.get(x) for x in ('title', 'author')):
        return {'success': False}, 400
    tier['added'] = datetime.now()
    id, = db.create_tier(**tier)
    return {'success': True, 'id': id}, 200

@app.route('/tiers/<int:id>')
def tier_by_id(id: int):
    tier = db.tier_by_id(id)
    if not tier:
        abort(404)
    return render_template('tier.jinja', tiers=tier, author=tier[0][1])

if __name__ == '__main__':
    wsgi = WSGIServer(('0.0.0.0', int(os.environ.get('PORT'))), app)
    wsgi.serve_forever()

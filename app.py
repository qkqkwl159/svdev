from flask import Flask, jsonify
from models import Stores

app = Flask(__name__)
@app.route('/')
def select():
    db = Stores.conn()
    data = Stores.db_sel(db)
    return jsonify(data)



@app.route('/json')
def jsondata():
    db = Stores.conn()
    data = Stores.db_sel(db)
    return jsonify(Stores.jsondata(data))
from flask import Flask, jsonify, request, render_template
from models import Stores

app = Flask(__name__)
@app.route('/')
def select():
    db = Stores.conn()
    data = Stores.db_sel(db)
    return jsonify(data)



@app.route('/insert', methods=['GET','POST'])
def insert():
    if request.method == 'POST':
        db = Stores.conn()
        eye = request.form.get('eye')
        mouth = request.form.get('mouth')
        
        print(eye, mouth)
        Stores.db_insert(db,eye,mouth)
        return render_template('post.html')
    else:

        return render_template('index.html')

    # db = Stores.conn()
    # data = Stores.db_sel(db)
    # return jsonify(Stores.jsondata(data))
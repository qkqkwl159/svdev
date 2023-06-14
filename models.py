import pymysql, requests, json 
from flask import jsonify
from datetime import datetime
class Stores():
    def conn():
        db = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='bbang',charset='utf8') 
        return db

    def db_sel(db):

        cursor = db.cursor()
        cursor.execute("SELECT * FROM USERS")
        result = cursor.fetchall()
        print(result)
        db.close()
        return  result

    def db_insert(db,eyeCNT,yCNT):
        cursor = db.cursor()
        timenow = datetime.now()
        strtimenow = timenow.strftime('%y-%m-%d %H:%M:%S')

        sql = f"INSERT INTO INFO VALUES({eyeCNT},{yCNT}, '{strtimenow}')"
        cursor.execute(sql)
        db.commit()

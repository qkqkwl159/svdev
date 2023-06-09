import pymysql, requests, json 
from flask import jsonify
class Stores():
    def conn():
        db = pymysql.connect(host='localhost', port=3306, user='root', passwd='14759', db='bbang',charset='utf8') 
        return db

    def db_sel(db):
        cursor = db.cursor()
        cursor.execute("SELECT * FROM USERS")
        result = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]
        print(column_names)


        result_dict_list = []
        for row in result:
            row_dict = dict(zip(column_names, row))


            result_dict_list.append(row_dict)
        
#        json_data = json.dumps(result_dict_list)

        db.close()
        return  result_dict_list

    def db_insert(db,eyeCNT,yCNT):
        cursor = db.cursor()
        sql = f"INSERT INTO  SLEEPINFO VALUES({eyeCNT},{yCNT})"
        cursor.execute(sql)
        db.commit()

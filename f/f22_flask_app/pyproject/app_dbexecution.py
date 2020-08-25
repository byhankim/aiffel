from flask import Flask, render_template, request
import os
import sqlite3
import pandas as pd


app = Flask(__name__)

'''
DB 함수
'''
def get_db(db_name):
    return sqlite3.connect(db_name)

def sql_command(conn, command):

    try:

        conn.execute(command)
        conn.commit()
        command = command.lower()

        if "select" in command:

            command_split = command.split(" ")
            select_command = "SELECT * FROM " + command_split[command_split.index("from")+1]
            df = pd.read_sql(select_command, conn, index_co=None)

            conn.close()

            return html
        
        conn.close()

        return True
    
    except :

        conn.close()

        return False

'''
File upload
'''
@app.route("/")
def index():
    return render_template("dbexecution.html")

@app.route("/dbsql")
def sql_preprocessing():
    if request.method=="POST":

        con = get_db(request.form.get("db_name"))
        sql = request.form.get("sql")
        res_sql = sql_command(con, sql)

        if res_sql == False:
            return render_template("dataexecution.html", label="비정상")
        elif res_sql == True:
            return render_template("dataexecution.html", label="정상작동")
        else:
            res_sql = "<html><body> " + res_sql + "</body></html>"



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=os.environ.get('PORT', 3000))
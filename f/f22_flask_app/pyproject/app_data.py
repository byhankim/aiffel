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

    try :

        conn.execute(command)
        conn.commit()
        command = command.lower()

        if "select" in command:

            command_split = command.split(" ")
            select_command = "SELECT * FROM " + command_split[command_split.index("from")+1]
            df = pd.read_sql(select_command, conn, index_col=None)
            html = df.to_html()

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
@app.route("/index")
def index():
    return render_template('data.html')

@app.route('/dbsql', methods=['POST'])
def sql_processing():
    if request.method == 'POST':

        con = get_db(request.form.get('db_name'))
        sql = request.form.get('sql')
        result_sql = sql_command(con, sql)

        if result_sql == False :
            return render_template('data.html', label="비정상")

        elif result_sql == True :
            return render_template('data.html', label="정상 작동")

        else :
            result_sql = "<html><body> " + result_sql + "</body></html>"
            return result_sql

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=os.environ.get('PORT', 3000))
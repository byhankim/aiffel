from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "플라스크 동작 확인!"

if __name__=="__main__":
    app.run()

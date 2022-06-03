from flask import Flask,render_template,request
import pymysql

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("home.html")


@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/movie')
def movie():
    conn = pymysql.connect(host="192.168.29.128", port=3306, user="root", password="123", database="PaChong",
                           charset="utf8")
    cur = conn.cursor()
    sql = "select * from students"
    cur.execute(sql)
    all = cur.fetchall()

    return render_template("movie.html",data_list =all)


@app.route('/score')
def score():
    return render_template("index.html")


@app.route('/word')
def word():
    return render_template("index.html")


@app.route('/team')
def team():
    return render_template("index.html")



if __name__ == '__main__':
    app.run(debug=True)


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
    cur.close()
    conn.close()

    return render_template("movie.html",data_list =all)


@app.route('/score')
def score():
    conn = pymysql.connect(host="192.168.29.128", port=3306, user="root", password="123", database="PaChong",
                           charset="utf8")
    cur = conn.cursor()
    sql = "select movie_score,count(movie_score) from students group by movie_score;"
    cur.execute(sql)
    all = cur.fetchall()
    score_list = []
    count_list = []
    for i in all:
        score_list.append(i[0])
        count_list.append(i[1])
    print(score_list)
    print(count_list)

    cur.close()
    conn.close()
    return render_template("score.html",score_list = score_list,count_list=count_list )


@app.route('/word')
def word():
    return render_template("wordcloud.html")


@app.route('/team')
def team():
    return render_template("team.html")



if __name__ == '__main__':
    app.run(debug=True)


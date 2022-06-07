import pymysql


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


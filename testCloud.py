import jieba
from matplotlib import pyplot as plt
from wordcloud import wordcloud
from PIL import Image
import numpy as np
import pymysql

# 提取一句话描述信息，并拼接成一个长字符串
conn = pymysql.connect(host="192.168.29.128", port=3306, user="root", password="123", database="PaChong",
                           charset="utf8")
cur = conn.cursor()
sql = "select movie_des from students;"
cur.execute(sql)
all = cur.fetchall()

text = ""
for i in all:
    text = text + i[0]
print(text)

cur.close()
conn.close()

# 结合特定图片，合成词云图片

cut = jieba.cut(text)
string = " ".join(cut)
print(string)

img = Image.open("static/assets/img/tree.jpg")
img_array = np.array(img)
wc = wordcloud.WordCloud(background_color="white",mask=img_array,font_path="msyh.ttc").generate_from_text(string)

fig = plt.figure(1)
plt.imshow(wc)
plt.axis("off")
plt.savefig("static/assets/img/wc.jpg",dpi=500)


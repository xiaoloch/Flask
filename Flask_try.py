from flask import Flask,render_template,request
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return "你好 世界"

# 通过路径传参，所有“/<字符串>”样式的路径都归类到这里
@app.route("/<name>")
def get_str(name):
    return "Hello %s" % name

# 通过路径传参，所有“/<整数>”类型的路径都归类到这里
@app.route("/<int:id>")
def get_id(id):
    return "你的学号是%d" %id

# 通过路径传参，所有“/<浮点数>”类型的路径都归类到这里
@app.route("/<float:fl>")
def get_float(fl):
    return "你的学号是%f" %fl

# 向页面传递一个变量
@app.route("/test")
def template():
    time = datetime.date.today() # 传递普通变量
    list = ["小明","小刚","小红","小丽"] # 传递列表变量
    form = {"本田":"思域","丰田":"卡罗拉","别克":"威朗","大众":"速腾"}
    return render_template("Jinjia2_template.html", time = time, list = list, form = form)

# 表单提交
@app.route("/register")
def regiser():
    return render_template("register.html")

# 表单接收与处理
@app.route("/form",methods=["POST","GET"])
def form():
    if request.method == "POST":
        input = request.form
        print(input)
        return render_template("form.html",input = input)

if __name__ == '__main__':
    app.run(debug=True)


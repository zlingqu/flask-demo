from flask import Flask
from flask import request,redirect
from flask import render_template
import json
from werkzeug.utils import secure_filename 

app = Flask(__name__,
            static_url_path="/python", #静态资源的url前缀，默认是static
            static_folder="static", #存放静态资源的目录名称，默认是static
            template_folder="templates")  #存放模板文件的目录名称，默认是templates


@app.route("/string")
def sayHello():
    return "直接返回字符"

@app.route("/index")
@app.route("/tmplate") #同一个试图可以对应多个路由
def renderView():
    return render_template("index.html")

@app.route("/")
def root():
    url="/index"
    return redirect(url) #重定向，参数直接写对应的路径名即可


@app.route('/center/add',methods=["GET","POST"])  # 代表个人中心页
def center():  # 视图函数
    if request.method == 'GET':  # 请求方式是get
        name = request.args.get('name')  # args取get方式参数
        age = request.args.get('age')
        hobby = request.args.getlist('hobby')  # getlist取一键多值类型的参数
        t = {"name": name,
             "age": age,
             "hoddy": hobby}
        # return "姓名：%s 年龄：%s 爱好：%s" % (name, age, hobby)
        return json.dumps(t, ensure_ascii=False)
    if request.method=="POST":
        return json.dumps({"message":"请求方法是post，返回错误"},ensure_ascii=False)


@app.route("/test",methods=["GET","POST"])
def post():
    headerMap={}
    for i in request.headers: #将header转为map类型
        headerMap[i[0]]=i[1]
    headerMap["EnvironHeaders"]=str(request.headers.environ)
    
    msg={
        "path": request.path,
        "full_path": request.full_path,
        "url": request.url,
        "base_url": request.base_url,
        "url_root": request.url_root,
        "host_url": request.host_url,
        "host":request.host,
        "query_string": str(request.query_string),
        "method": request.method,
        "headers": headerMap,
        "charset":request.charset,
        "shallow":request.shallow,
        "view_args":request.view_args,
        "url_rule":str(request.url_rule),
        "environ": str(request.environ)
    }
    # print(request.__dict__)
    return json.dumps(msg,ensure_ascii=False)

# 返回post的body数据
@app.route("/data/", methods=["POST"])
def request_data():
    data = request.data
    print(type(data))   # <class 'bytes'>
    return data


# 返回请求的表单参数
@app.route("/form/", methods=["POST"])
def request_form():
    form = request.form
    print(form)         
    name = form.get("name") #获取表单的单个值
    age = form.get("age")
    # return F"{name},{age}"
    return json.dumps(form.to_dict()) #to_dict()方法将表单转换为map
    # return json.dumps(dict(form.lists()))


# 获取请求中的cookies信息
@app.route("/cookies/")
def request_cookies():
    cookie_name = request.cookies.get("cookie_name")
    return F"cookies:{cookie_name}"
    # return json.dumps(cookies.to_dict())


# 文件上传
# 限制文件大小为16M，如果超过16M，Flask 会抛出一个 RequestEntityTooLarge 异常
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
@app.route("/files/", methods=["POST"])
def request_files():
    files=request.files
    # 获取文件对象
    file = files.get("file")    # postman上使用post，form-data类型，名字叫：file，选file类型，值选择某个文件即可
    if file is None:
        return "未上传文件"
    # 获取文件的名字
    filename = file.filename    # 1.jpg
    # 解决文件名伪造问题，比如文件名是  ../../../../etc/passwd 等情况
    filename = secure_filename(filename)

    # 将文件保存到本地
    # 1、使用python的open方法
    # with open("./" + filename, "wb") as f:
    #     # 读取上传的文件
    #     file_content = file.read()
    #     # 写入到本地文件
    #     f.write(file_content)

    # 2、使用flask封装的save方法
    file.save("./" + filename)
    return "上传成功"



if __name__ == '__main__':
    print(app.url_map) # 通过url_map可以查看整个flask中的路由信息
    app.run()

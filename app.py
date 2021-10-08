from flask import Flask
from flask import request,redirect,abort,Response,make_response,session
from flask import render_template
import json
from werkzeug.utils import secure_filename 
from route import create_app

app = create_app()

if __name__ == '__main__':
    print(app.url_map) # 通过url_map可以查看整个flask中的路由信息
    app.run()

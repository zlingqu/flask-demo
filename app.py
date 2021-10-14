from flask import Flask

# from route_flask import add_route
# from route_flask import add_route

app = Flask(__name__,
            static_url_path="/python",  # 静态资源的url前缀，默认是static
            static_folder="static",  # 存放静态资源的目录名称，默认是static
            template_folder="templates")  # 存放模板文件的目录名称，默认是templates

# session通过密钥对数据进行签名以加密数据，因此,设置session前得先设置一个密钥。密钥可以随便输入。
app.secret_key = 'dsaX5Yfdliwx'

from route_flask import add_route  # 使用flask原生方法管理路由

add_route(app)
from route_flask_restful import add_route  # 使用flask_restful管理路由

add_route(app)

if __name__ == '__main__':
    a = "xx_yy_zz"
    b = a.split('_', 1)[1]
    print(b)
    # print(app.url_map)  # 通过url_map可以查看整个flask中的路由信息
    app.run(port=80)

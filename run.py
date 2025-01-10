from flask import Flask
from gevent import pywsgi
import socket
import threading

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

def udp_server(host, port):
    """
    启动 UDP 服务器
    """
    udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_sock.bind((host, port))

    while True:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        data, addr = udp_sock.recvfrom(1024)  # 接收数据
        # print(f"Received from {addr}: {data.decode()}")
        # 响应数据
        reply = 'my ip is {}'.format(local_ip)
        udp_sock.sendto(reply.encode('utf-8'), addr)
        # udp_sock.sendto(data, addr)


def run_tcp_server():
    """
    启动 TCP 服务器
    """
    app.debug = True

    server = pywsgi.WSGIServer(
        listener = ('0.0.0.0', 8888),
        application=app)
    print("TCP server started on 0.0.0.0:8888")
    server.serve_forever()
    

if __name__ == '__main__':
    # 启动 UDP 服务线程
    udp_thread = threading.Thread(target=udp_server, args=('0.0.0.0', 9999), daemon=True)
    print("UDP server started on 0.0.0.0:9999")
    udp_thread.start()

    # 启动 TCP 服务（主线程）
    run_tcp_server()
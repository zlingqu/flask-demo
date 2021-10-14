from flask_restful import Api, Resource
from flask import request


def add_route(app):
    api = Api(app)

    class HelloWorld(Resource):
        def get(self):
            payload = request.args.to_dict()
            if len(payload) == 0:
                res = {'hello': 'world'}
            else:
                res = payload

            return res

        def delete(self):  # 不同发方法对应不同的http的method
            return {'hello': 'deleted'}, 201  # 可以自定义http状态码

    class HelloWorld2(Resource):
        def get(self):
            return {'hello': 'world'}

    api.add_resource(HelloWorld, '/restful')  # 第一个参数是类名，第二个是path
    api.add_resource(HelloWorld2, '/restful1', '/restful2')  # 多个URI对应一个class

'''The main building block provide by Flask-RestX are resources. 
Resources are build on top of flask pluggable view, giving access to multipe http
'''
from flask import Flask, request
from flask_restx import Resource, Api 
from requests import put, get # -> This is for request library

app = Flask(__name__)
api = Api(app)

todos = {}

@api.route('/<string:todo_id>')
class TestApi(Resource): 
    def get(self, todo_id):
        return {todo_id : todos[todo_id]}
    
    def put(self, todo_id):
        todos[todo_id] = request.form['data'] 
        return {todo_id : todos[todo_id]}
    
# Flask-RESTX understands multiple kinds of return values form view method 
# Flask-RestX also support setting the response code and response headers using multiple retrurn values
@api.route('/test_api1')
class TestApi1(Resource): 
    def get(self):
        # Default 200 Ok 
        return {'TestApi1' : 'Test Api 1 its Ok'}
    
@api.route('/test_api2')
class TestApi2(Resource): 
    def get(self): 
        return {'Key API  ' : 'Success Get API 2'}, 201
    
@api.route('/test_api3')
class TestApi3(Resource): 
    def get(self): 
        return {'Task Api 3' : 'Task Api 3'}, 201, {'Etag' : 'Some String'}

'''
Endpoint -> many times in API resources will have multiple urlS
You can pass multiple URLs to the add_resource() or route() decorator
'''
# @app.route('/testing', '/multi')
# class multiple_url(Resource): 
#     def get(self): 
#         return {'key api' : 'value API'}

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask 
from flask_restx import Resource, Api 

app = Flask(__name__)
api = Api(app)

@api.route('/test_api')
class TestApi(Resource):
    def get(self): 
        return {'Key Api' : 'Value Of Api'}

if __name__ == '__main__': 
    app.run(debug=True)

from flask import Flask 
from markupsafe import escape 

app = Flask(__name__)
#Routing Page -> Use the route() decorator for bind a function to A url 
@app.route('/')
def index(): 
    return 'Index of page'

@app.route('/Hello')
def hello(): 
    return 'Hello World'

@app.route("/Halo")
def hello_world():
    return "<p>Hello World</p>"

@app.route("/<name>")
def testing_escaping(name): 
    return f"Hello, {escape(name)}"

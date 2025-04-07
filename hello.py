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

# Variables Rules 
# Can add variable sections to url by marking sections with <variable_name>
@app.route('/user/<username>')
def show_user_profile(username): 
    #Show user profile for that user 
    return f"Username is :  {escape(username)}"

@app.route('/post/<int:post_id>')
def show_post(post_id): 
    # Show the post with the given id the given id is integer 
    return f"The post id is {post_id}"

@app.route('/path/<path:subpath>')
def sub_path(subpath): 
    # Show the subpath after path 
    return f"The Subpath is {escape(subpath)}"
'''
Type of converter types : 
string -> (default) accept any text without slash 
int -> accept possitive integer 
float -> accepts positive floating point values 
path -> like string but also accept slashes 
uuid -> accepts UUID strings 
'''

# Unique url / redirection 
@app.route('/projects/')
def projects(): 
    return 'This is the project page.'

@app.route('/about')
def about(): 
    return 'This is an about page'

@app.route('/contact')
def contact(): 
    return 'this is an contact page'
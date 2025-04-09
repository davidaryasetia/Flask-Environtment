
from flask import Flask, url_for, request, render_template #-> We can use multiple import like this
from markupsafe import escape 


app = Flask(__name__)


# Routing page 
@app.route('/')
def index(): 
    return render_template('index.html')

@app.route("/test")
def testing(): 
    return "Test package"

'''
2. Variables rules  -> <converter:variable_name> 
string -> default accept text without slash 
int -> accept positive integer 
float -> accept positive floating point 
path -> like string but also accept slash 
uuid -> accept uuid string
'''

# example string
@app.route('/username/<username>')
def username_account(username): 
    return f'User Account {escape(username)}'

# example of integer 
@app.route('/post/<int:post_id>')
def post_id(post_id): 
    return f'Post ID: {escape(post_id)}'

# example of path 
@app.route('/path/<path:subpath>')
def path_id(subpath): 
    return f'Path ID : {escape(subpath)}'


# 3. Unique URLs redirection -> the following two rules differ in their ussage trailing slash 
@app.route('/projects/')
def end_trailing_space(): 
    return 'Use the trailing space'

# different with this 
# Kalau akses pakek ini /about/ -> maka dia not found 
@app.route('/about')
def another_route(): 
    return f'With about route'


# URL Building -> to build url to a specific function. use url_for()


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
    return 'this is an contact page '


# 4. URL Building -> To build url to a specific function, use url_for()
# wE use a test_request_context() => to tells flask to behave as thought its handling a requuest
# with app.test_request_context(): 
#     print(url_for('test'))
#     print(url_for('project'))


# 5. HTTPS Methods -> web application use different HTTP methods when accessing URLs.
# By default http method route in flask use the GET REQUEST. 
# example 
@app.route('/login', methods=['GET', 'POST'])
def login(): 
    if request.method == 'POST': 
        return 'This method is used for Post and register Application'
    else: 
        return 'This method is used for POST and register Application'
'''
The example above keeps all methods for the route within one function. 
Flask also provide decorating such as routes with get() and post()
'''
@app.get('/signing')
def signing(): 
    return 'The get request method to show the login form'

# If i used to access this in browser it's user a message that "Method Not Allowed
@app.post('/register')
def register(): 
    return 'The register post metho function'

# Using a static file 
'''
Dynamic web application also need static files . You can call static files 
like this. 
This can be used to static file style.css
'''

# if __name__ == '__main__': 
#     app.run(debug=True)


# Rendering the template
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('index.html', person=name)


# The request object section => method GET and POST
@app.route('/login', method=['GET', 'POST'])
def login_account(): 
    error = None
    if request.method == 'POST':
        if valid.login(
            request.form['username'], 
            request.form['password']
        ): 
            return log_the_user_in(request.form['username'])
        else: 
            error = 'Invalid username/password'
            return render_template('login.html', error=error)
This project is use to learn new environtment technologies in Flask In 3 Chapters : 
1. Fundamentals Of Flask :  
    This chapter is learn from fundamentals flask from basic original flask documentation, and implement, how to code, and syntax about flask. 

2. api : 
    This chapter is learn for Fundamentals and developing rest api with flask-restx from original documentation and implement few code. This code is build API that using a flask-resk. That implemented how to testing an API from Flask-restx environtment using a sweager. 

3. Build Miniproject to Build Rest-API with Flask Framework, that a real connection from My Database Server. 
In the configuration Database project in : 
- app.py
- db.py 
- config.json

With a real Database Server Of postgresql
host : projectdev.site
user : postgres
password : Okokokdalll1
db : db_flask
port : 5432

To Run Mini Program Flask API : 
1. Instalation Requirements -> pip -r requirements.txt
2. running python app for mini project-> python app.py 
3. Endpoint Rest API with Flask API : 
    Method : GET 
    URL Endpoint : http://127.0.0.1:5000/read
    -------------------------------------------------
    Method : POST 
    URL Endpoint : http://127.0.0.1:5000/write
    Raw Parameter for Body : 

    {
    "name" : "Michael", 
    "job_profile" : "Programmer", 
    "phone" : "656565556565"
    }

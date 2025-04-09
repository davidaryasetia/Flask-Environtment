# Build simple Flask app with read and write routes
from flask import Flask, request, jsonify
import db
import json

app = Flask(__name__)

# Load configuration from the JSON file 
with open('config.json', 'r') as file:
    config = json.load(file)

db_table = config['postgres'].get("db_table")

@app.route('/')
def home(): 
    return 'Welcome to the Flask Postgress App'

# Build Flask API Convensional 
# Flask App Table 
@app.route('/read', methods=['GET'])
def read(): 
    query = f'SELECT * FROM {db_table};'
    try: 
        result = db.read_from_db(query)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error' : str(e)}), 500
    
@app.route('/write', methods=['POST'])
def write(): 
    query = f'INSERT INTO {db_table} (name, job_profile, phone) VALUES (%s, %s, %s);'
    params = (data['name'], data['job_profile'], data['phone'])
    try:
        db.write_to_db(query, params)
        return jsonify({'message' : 'Data Insert successfuly!'})
    except Exception as e:
        return jsonify({'error' : str(e)}), 

if __name__ == '__main__': 
    app.run(debug=True)
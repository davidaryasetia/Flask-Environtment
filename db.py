import psycopg2
import json
# load configuration from JSON file
with open('config.json', 'r') as file:
    config = json.load(file)

# DB Configuration 
db_config = config['postgres']

#  This is for creates a connection to PostgreeSQL Database using credentials db_config.json
def get_db_connection(): 
    connection = psycopg2.connect(
        host=db_config['host'], 
        port=db_config['port'], 
        database=db_config['database'], 
        user=db_config['user'], 
        password=db_config['password']
    )
    return connection

# This function to takes SQL Query and optional parameter(params)
def read_from_db(query, params=None):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, params)
    result = cursor.fetchall()
    cursor.clone()
    conn.close()
    return result

# This function is to insert update or delete records in the database.
def write_to_db(query, params=None):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    cursor.close()
    conn.close()
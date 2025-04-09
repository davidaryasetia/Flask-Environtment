'''
Response Marshalling -> Basic Usage (you  can define a dict or orderedDict)
'''
from flask import Flask 
from flask_restx import Resource, fields, Api
from datetime import datetime


@api.route('/todo')
class Todo(Resource):

app = Flask(__name__)
api = Api(app)

model = api.model('Model', {
    'name' : fields.String, 
    'address' : fields.String, 
    'date_updated' : fields.DateTime(dt_format='rfc822'), 
})

# Dummy function untuk simulasi DB 
def db_get_todo(): 
    return {
        'name' : 'John Lobo', 
        'address' : '123 st main', 
        'dt_updated' : datetime.now()
    }

@api.route('/todo')
class Todo(Resource): 
    @api.marshal_with(model, envelope='resource')
    def get(self): 
        return db_get_todo()
    
if __name__ == '__main__': 
    app.run(debug==True)
'''
Model is used for assumes that you have a custom database object(todo) that
has attribute name, address, and data_updated. d    
'''


# Renaming Attributes -> Often times your public facing field name is different from your internal field name. 
model = {
    'name' : fields.String(attribute='private_name'), 
    'address' : fields.String, 
}

# Lambda or any callable can also be specified as attribute
model = {
    'name' : fields.String(attribute=lambda. x: x._private_name), 
    'address' : fields.String
}


# Default Value -> If for some reason data object doesnt have attribut in field list, you can specify a default value to return instead Of None
# Implementating of default value 
model = {
    'name' : fields.String(default='Anonymus Function')
    'address' : fields.String
}

# The api.model() factory
# The model() factory allow you to instantiate amd register models to your API or namespace
my_Fields = api.model('MyModel', {
    'name' : fields.String, 
    'age' : fields.Integer(min=0)
})

# Equivalent to
my_Fields = Model('myModel', {
    'name' : fields.String, 
    'age' : fields.integer(min=0)
})
api.models[my_fields.name] = my_Fields

# Duplicating with clone -> The Model.clone() method allows you to instantiate an augmented model
parent = Model('Parent', {
    'name' : fields.String
})

child = api.clone('Child', parent, {
    'age' : fields.Integer
})
'''
Data Formatting -> By Default, all fields in your return iterable will be 
renderer as is

Data Formatting : 

'''
from flask import Flask
from flask_restx import fields, Api, Resource

app = Flask(__name__)
api = Api(app)

model = api.model('Model', {
    'task' : fields.String, 
    'uri' : fields.Url('todo_ep')
})

class TodoDao(object): 
    def __init__(self, todo_id, task): 
        self.todo_id = todo_id
        self.task = task

        self.status = 'active'

@api.route('/todo')
class Todo(Resource): 
    @api.marshal_with(model)
    def get(self, **kwargs): 
        return TodoDao(todo_id='my_todo', task='Remember the milk')
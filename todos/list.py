import json
import os

from snippets import log_event
from models.todo_model import TodoModel


def todo_list(event, context):
    log_event(event)
    # fetch all todos from the database
    Todo = TodoModel(os.environ['DYNAMODB_TABLE'])
    todos = Todo.list()

    # create a response
    return {'statusCode': 200,
            'body': json.dumps({'todos': [dict(result) for result in todos]})}

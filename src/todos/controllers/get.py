import json
import os
from models.todo_model import TodoModel
from snippets import response


def get_todo(event, context):
    todo = TodoModel()
    id = event.get('pathParameters').get('id')
    todo.get(id)

    # create a response
    if todo:
        return response(200, json.dumps(dict(todo)))
    else:
        return response(204, "Record not found")


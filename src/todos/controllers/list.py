import json
import os

from snippets import log_event, response
from models.todo_model import TodoModel


def list_todo(event, context):
    log_event(event)
    # fetch all todos from the database
    Todo = TodoModel()
    todos = Todo.list()

    # create a response
    return response(200, json.dumps({'todos': [dict(result) for result in todos]}))
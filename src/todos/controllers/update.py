import json
import logging
import os

from snippets import log_event, response
from models.todo_model import TodoModel



def update_todo(event, context):
    log_event(event)
    todo = TodoModel()
    id = event.get('pathParameters').get('id')
    data = json.loads(event['body'])
    updated = todo.update(id, data)

    # create a response
    return response(200,json.dumps(dict(updated)))


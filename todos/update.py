import json
import logging
import os

from snippets import log_event, response
from models.todo_model import TodoModel


def update(event, context):
    log_event(event)
    todo = TodoModel(os.environ['DYNAMODB_TABLE'])
    itemId = event.get('pathParameters').get('itemId')
    data = json.loads(event['body'])
    todo.update(itemId, data)

    # create a response
    return response(200,json.dumps(dict(todo)))


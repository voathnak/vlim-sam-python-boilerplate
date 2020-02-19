import json
import logging
import os

from snippets import log_event
from models.todo_model import TodoModel


def update(event, context):
    log_event(event)
    todo = TodoModel(os.environ['DYNAMODB_TABLE'])
    itemId = event.get('pathParameters').get('itemId')
    data = json.loads(event['body'])
    todo.update(itemId, data)

    # create a response
    return {'statusCode': 200,
            'body': json.dumps(dict(todo))}


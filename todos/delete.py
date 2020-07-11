import json
import os
from models.todo_model import TodoModel
from snippets import response


def delete(event, context):
    todo = TodoModel(os.environ['DYNAMODB_TABLE'])
    itemId = event.get('pathParameters').get('itemId')
    todo.delete(itemId)

    # create a response
    return response(204)

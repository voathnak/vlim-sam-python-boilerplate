import json
import os
from models.todo_model import TodoModel
from snippets import response


def get(event, context):
    found_todo = TodoModel(os.environ['DYNAMODB_TABLE'])
    itemId = event.get('pathParameters').get('itemId')
    found_todo.get(itemId)

    # create a response
    if found_todo:
        return response(200, json.dumps(dict(found_todo)))
    else:
        return response(204, "Record not found")


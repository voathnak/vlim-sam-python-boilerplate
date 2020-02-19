import json
import os
from models.todo_model import TodoModel


def get(event, context):
    found_todo = TodoModel(os.environ['DYNAMODB_TABLE'])
    itemId = event.get('pathParameters').get('itemId')
    found_todo.get(itemId)

    # create a response
    if found_todo:
        response = {
            'statusCode': 200,
            'body': json.dumps(dict(found_todo))
        }
    else:
        response = {
            'statusCode': 204,
            'body': "Record not found"
         }

    return response

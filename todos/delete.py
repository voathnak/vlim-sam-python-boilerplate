import json
import os
from models.todo_model import TodoModel


def delete(event, context):
    todo = TodoModel(os.environ['DYNAMODB_TABLE'])
    itemId = event.get('pathParameters').get('itemId')
    todo.delete(itemId)

    # create a response
    return {'statusCode': 204}

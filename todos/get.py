import json
import os
from models.todo_model import TodoModel


def get(event, context):
    found_todo = TodoModel(os.environ['DYNAMODB_TABLE'])
    found_todo.get(event.get('pathParameters').get('itemId'))

    # create a response
    return {'statusCode': 200,
            'body': json.dumps(dict(found_todo))}

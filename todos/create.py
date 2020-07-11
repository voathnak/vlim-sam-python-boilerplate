import json
import logging
import os
from models.todo_model import TodoModel
from snippets import response


def lambda_handler(event, context):
    data = json.loads(event['body'])
    if 'text' not in data:
        logging.error('Validation Failed')
        return response(422,json.dumps({'error_message': 'Couldn\'t create the todo item.'}))

    if not data['text']:
        logging.error('Validation Failed - text was empty. %s', data)
        return response(422,json.dumps({'error_message': 'Couldn\'t create the todo item. As text was empty.'}))

    a_todo = TodoModel(os.environ['DYNAMODB_TABLE'])

    # write the todo to the database
    a_todo.save({
        "text": data['text'],
        "checked": False
    })

    # create a response
    return response(201, json.dumps(dict(a_todo)))

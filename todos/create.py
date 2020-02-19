import json
import logging
import os
from models.todo_model import TodoModel


def lambda_handler(event, context):
    data = json.loads(event['body'])
    if 'text' not in data:
        logging.error('Validation Failed')
        return {'statusCode': 422,
                'body': json.dumps({'error_message': 'Couldn\'t create the todo item.'})}

    if not data['text']:
        logging.error('Validation Failed - text was empty. %s', data)
        return {'statusCode': 422,
                'body': json.dumps({'error_message': 'Couldn\'t create the todo item. As text was empty.'})}

    a_todo = TodoModel(os.environ['DYNAMODB_TABLE'])

    # write the todo to the database
    a_todo.save({
        "text": data['text'],
        "checked": False
    })

    # create a response
    return {'statusCode': 201,
            'body': json.dumps(dict(a_todo))}


import json
import logging
from models.todo_model import TodoModel
from snippets import response


def create_todo(event, context):
    data = json.loads(event['body'])
    if 'text' not in data:
        logging.error('Validation Failed')
        return response(422,json.dumps({'error_message': 'Couldn\'t create the todo item.'}))

    if not data['text']:
        logging.error('Validation Failed - text was empty. %s', data)
        return response(422,json.dumps({'error_message': 'Couldn\'t create the todo item. As text was empty.'}))

    todo = TodoModel()

    # write the todo to the database
    test = todo.create({
        "text": data['text'],
        "checked": False
    })

    # create a response
    return response(201, json.dumps(dict(todo)))

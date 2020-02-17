import json

import todo_model as TodoModel


def todo_list(event, context):
    # fetch all todos from the database
    results = TodoModel.scan()

    # create a response
    return {'statusCode': 200,
            'body': json.dumps({'items': [dict(result) for result in results]})}

import json
import os
from models.user_model import UserModel
from snippets import response, log_event


def lambda_handler(event, context):
    log_event(event)
    values = json.loads(event.get('body'))

    user = UserModel(os.environ['DYNAMODB_TABLE'])

    # write the user to the database
    user.save(values)

    # create a response
    if user:
        return response(201, json.dumps([dict(user)]))
    else:
        return user.error_response


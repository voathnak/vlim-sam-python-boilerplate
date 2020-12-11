import json
import os
from models.user_model import UserModel
from snippets import response, log_event


def lambda_handler(event, context):
    log_event(event)
    values = json.loads(event.get('body'))

    user = UserModel()

    # write the user to the database
    user.create(values)

    # create a response
    if user:
        return response(201, json.dumps([dict(user)]))
    else:
        return user._error_response


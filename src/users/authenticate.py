import json
import os
from models.user_model import UserModel
from snippets import log_event, response


def authenticate_handler(event, context):
    log_event(event)
    user_data = json.loads(event.get('body'))
    User = UserModel(os.environ['DYNAMODB_TABLE'])
    users = [user for user in User.list() if
             user.username == user_data.get("username") and user.password == user_data.get("password")]

    # create a response
    if users:
        return response(200, json.dumps([{
                    "id": users[0].itemId,
                    "username": users[0].username,
                    "firstName": users[0].firstName,
                    "lastName": users[0].lastName,
                    "token": 'fake-jwt-token'
                }]))
    else:
        return response(204, json.dumps(
            {
                'body': "Record not found"
            }
        ))

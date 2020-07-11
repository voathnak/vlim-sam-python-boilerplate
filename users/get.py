import json
import os
from models.user_model import UserModel
from snippets import response


def get(event, context):
    found_user = UserModel(os.environ['DYNAMODB_TABLE'])
    itemId = event.get('pathParameters').get('itemId')
    found_user.get(itemId)

    # create a response
    if found_user:
        return response(200, json.dumps(dict(found_user)))
    else:
        return response(204, "Record not found")


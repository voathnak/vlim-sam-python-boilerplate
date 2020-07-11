import json
import os

from snippets import log_event, response
from models.user_model import UserModel


def user_list(event, context):
    log_event(event)
    # fetch all users from the database
    User = UserModel(os.environ['DYNAMODB_TABLE'])
    users = User.list()

    # create a response
    return response(200, json.dumps([dict(result) for result in users]))

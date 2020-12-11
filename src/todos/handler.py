import json

from controllers.delete import delete_todo
from controllers.get import get_todo
from snail.constants.http_status_code import METHOD_NOT_ALLOWED
from snippets import log_event, response

from controllers.create import create_todo
from controllers.list import list_todo
from controllers.update import update_todo


def lambda_handler(event, context):
    log_event(event)
    http_method = event.get('httpMethod')
    path = event.get('path')
    print("method/path", http_method, path)

    if http_method == "POST":
        return create_todo(event, context)
    elif http_method == "GET":
        if event.get("requestContext").get("path") == "/todos/{id}":
            return get_todo(event, context)
        return list_todo(event, context)
    elif http_method == "PUT":
        return update_todo(event, context)
    elif http_method == "DELETE":
        return delete_todo(event, context)

    return response(METHOD_NOT_ALLOWED, {"message": "Method not allowed"})

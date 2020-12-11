from models.todo_model import TodoModel
from snippets import response


def delete_todo(event, context):
    todo = TodoModel()
    id = event.get('pathParameters').get('id')
    status = todo.delete(id)
    if status:
        return response(204)
    return response(501, {"message": "delete failed"})

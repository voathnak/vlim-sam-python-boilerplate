from snail.Model import CoreModel


class TodoModel(CoreModel):

    _collection_name = "todos"

    def __init__(self):
        super(TodoModel, self).__init__()

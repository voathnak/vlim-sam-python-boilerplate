from snail.Model import CoreModel


class UserModel(CoreModel):

    _required_fields = ['email', 'firstName', 'lastName', 'username', 'password']
    _unique_key = ['username']
    _collection_name = "users"

    def __init__(self):
        super(UserModel, self).__init__()



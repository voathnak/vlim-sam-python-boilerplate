from models.Model import CoreModel


class UserModel(CoreModel):

    _required_fields = ['firstName', 'lastName', 'username', 'password']

    def __init__(self, table_name):
        super(UserModel, self).__init__(table_name)



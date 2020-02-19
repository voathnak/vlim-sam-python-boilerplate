import uuid
from datetime import datetime

import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')


class CoreModel:

    def __init__(self, table_name):
        self._table = dynamodb.Table(table_name)

    def save(self, values):

        timestamp = str(datetime.utcnow().timestamp())

        item = {
            'itemId': str(uuid.uuid1()),
            'createdAt': timestamp,
            'updatedAt': timestamp,
        }

        item.update(values)
        for key, value in item.items():
            self.__setattr__(key, value)

        # write the todo to the database
        self._table.put_item(Item=item)

    def get(self, itemId):
        try:
            item = self._table.get_item(Key={'itemId': itemId})
            for key, value in item.get('Item', []).items():
                self.__setattr__(key, value)
        except ClientError as e:
            print(e.response['Error']['Message'])

    def __iter__(self):
        iters = dict((x, y) for x, y in self.__dict__.items() if x[:1] != '_')
        for name, attr in iters.items():
            yield name, attr

    def __setattr__(self, name, value):
        if name == 'createdAt' or name == 'updatedAt':
            self.__dict__[name] = datetime.fromtimestamp(float(value)).strftime("%b %d %Y %H:%M:%S")
        else:
            self.__dict__[name] = value


import boto3


def initialize_db():
    db = boto3.resource('dynamodb')
    return db

# table = db.Table('test')
# print(table)
# response = table.put_item(Item={"id":2})
# print(response)

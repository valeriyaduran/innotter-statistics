import boto3


def initialize_db():
    db = boto3.resource('dynamodb')
    return db

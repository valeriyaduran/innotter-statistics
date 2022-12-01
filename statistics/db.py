import os

import boto3


def initialize_db():
    db = boto3.resource('dynamodb',
                        endpoint_url=os.getenv('DYNAMO_ENDPOINT'),
                        region_name=os.getenv('AWS_REGION'),
                        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
                        )
    return db

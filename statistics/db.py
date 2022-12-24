import boto3

from statistics.config import DYNAMO_ENDPOINT, AWS_DEFAULT_REGION, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY


def initialize_db():
    db = boto3.resource('dynamodb',
                        endpoint_url=DYNAMO_ENDPOINT,
                        region_name=AWS_DEFAULT_REGION,
                        aws_access_key_id=AWS_ACCESS_KEY_ID,
                        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
                        )
    return db


async def get_table():
    dynamodb = initialize_db()
    table = dynamodb.Table('Stats')
    return table


from statistics.db import initialize_db


def create_table():
    db = initialize_db()
    db.create_table(
        TableName='Stats',  # create table Stats
        AttributeDefinitions=[
            {
                'AttributeName': 'user_id',
                'AttributeType': 'N'  # with type string
            }
        ],
        KeySchema=[
            {
                'AttributeName': 'user_id',
                'KeyType': 'HASH'
            }
        ],
        ProvisionedThroughput={  # specyfing read and write capacity units
            'ReadCapacityUnits': 10,  # these two values really depend on the app's traffic
            'WriteCapacityUnits': 10
        }
    )


if __name__ == '__main__':
    create_table()

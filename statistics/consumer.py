import json
import logging

import boto3
import pika


class ReceiveMessagesService:
    @staticmethod
    def callback(ch, method, properties, body):
        """Runs on callback, when pika receives message"""
        response = json.loads(body)
        dynamodb = boto3.resource('dynamodb',
                                  endpoint_url='http://dynamodb:8002',
                                  region_name='us-east-1',
                                  aws_access_key_id='1234',
                                  aws_secret_access_key='1234'
                                  )
        table = dynamodb.Table('Stats')
        to_increase_counter = {"post_added": "posts", "page_added": "pages",
                               "like_added": "likes", "follow_request_added": "follow_requests",
                               "follower_added": "followers"}
        to_decrease_counter = {"post_deleted": "posts", "like_removed": "likes",
                               "follow_request_removed": "follow_requests"}
        if response["action"] in to_increase_counter:
            table.update_item(
                Key={
                    "user_id": response["user_id"]
                },
                UpdateExpression=f"ADD {to_increase_counter[response['action']]} :num",
                ExpressionAttributeValues={
                    ":num": 1
                },
            )
        elif response["action"] in to_decrease_counter:
            table.update_item(
                Key={
                    "user_id": response["user_id"]
                },
                UpdateExpression=f"ADD {to_decrease_counter[response['action']]} :num",
                ExpressionAttributeValues={
                    ":num": -1
                },
            )
        ch.basic_ack(delivery_tag=method.delivery_tag)

    @staticmethod
    def start_receiving_messages():
        try:
            credentials = pika.PlainCredentials(
                username='guest',
                password='guest'
            )
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(
                    host='rabbitmq',
                    credentials=credentials,
                ))
            channel = connection.channel()
            channel.queue_declare(queue='statistics', durable=True)
            channel.basic_consume(
                queue='statistics',
                on_message_callback=ReceiveMessagesService.callback
            )
            channel.start_consuming()
        except Exception as e:
            logging.exception(e)


if __name__ == '__main__':
    ReceiveMessagesService.start_receiving_messages()

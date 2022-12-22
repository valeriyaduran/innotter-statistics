import asyncio
import json
import logging
import pika

from statistics.registry import DynamoDBRegistry


class ReceiveMessagesService:
    @staticmethod
    def callback(ch, method, properties, body):
        """Runs on callback, when pika receives message"""
        response = json.loads(body)
        asyncio.run(DynamoDBRegistry.update_table_data(response))
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
                )
            )
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

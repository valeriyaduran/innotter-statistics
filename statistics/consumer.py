import json
import logging

import pika

from statistics.config import RABBIT_USERNAME, RABBIT_PASSWORD, RABBIT_HOST


class ReceiveMessagesService:
    @staticmethod
    def callback(ch, method, properties, body):
        """Runs on callback, when pika receives message"""
        response = json.loads(body)

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
                on_message_callback=ReceiveMessagesService.callback,
                auto_ack=True
            )
            channel.start_consuming()
        except Exception as e:
            logging.exception(e)


if __name__ == '__main__':
    ReceiveMessagesService.start_receiving_messages()

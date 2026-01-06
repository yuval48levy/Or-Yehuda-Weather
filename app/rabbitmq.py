from datetime import datetime
import os
import pika


def send_to_rabbitmq(temp):
    connection = pika.BlockingConnection(pika.URLParameters(os.getenv('RABBITMQ_URL')))
    channel = connection.channel()
    
    channel.queue_declare(queue='logs_queue')
    
    message = f"{temp}:{datetime.now()}"
    print(message)
    channel.basic_publish(exchange='',
                          routing_key='logs_queue',
                          body=message)
    
    connection.close()
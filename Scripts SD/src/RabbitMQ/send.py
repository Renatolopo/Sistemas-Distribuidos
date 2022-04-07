#!/usr/bin/env python
import pika
from time import sleep

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

# channel.basic_publish(exchange='',
#                         routing_key='hello',
#                         body=f'mensagen 3')

for i in range(10):
    sleep(2)
    channel.basic_publish(exchange='',
                        routing_key='hello',
                        body=f'nova mensagem {i}')
                  

print("Mensagem Enviada!")
connection.close()
 
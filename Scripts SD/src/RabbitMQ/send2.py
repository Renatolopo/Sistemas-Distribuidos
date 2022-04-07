#!/usr/bin/env python
import pika
from time import sleep

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='Fila2')

channel.basic_publish(exchange='',
                        routing_key='Fila2',
                        body=f'Mensagen 2')


print("Mensagem Enviada!")
connection.close()

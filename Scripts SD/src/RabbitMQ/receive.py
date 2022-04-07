#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print("Recebido a mensagem: %r" % body)

channel.basic_consume('hello', callback, auto_ack=True)

print('Esperando por uma mensagem. Para sair precione CTRL+C')
channel.start_consuming()
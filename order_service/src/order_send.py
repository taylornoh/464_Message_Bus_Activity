#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))


message_in = input("What order is complete?  ")
while(message_in != "exit"):
    channel = connection.channel()
    channel.queue_declare(queue='order->notification')

    channel.basic_publish(exchange='', routing_key='order->notification', body=message_in)
    print(" [x] Sent " + message_in)

    # also send to user
    channel = connection.channel()
    channel.queue_declare(queue='x->user')

    channel.basic_publish(exchange='', routing_key='x->user', body=message_in)
    print(" [x] Sent " + message_in)

    message_in = input("What order is complete?  ")

connection.close()
#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

message_in = input("Payment status: ")
while(message_in != "exit"):
    
    channel.queue_declare(queue='x->order')

    channel.basic_publish(exchange='', routing_key='x->order', body=message_in)
    print(" [x] Sent " + message_in)

    message_in = input("Payment status: ")

connection.close()
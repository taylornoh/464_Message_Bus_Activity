#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

message_in = input("Type in a username: ")
while(message_in != "exit"):
    
    channel.queue_declare(queue='user->product')

    channel.basic_publish(exchange='', routing_key='user->product', body=message_in)
    print(" [x] Sent " + message_in)

    message_in = input("Type in a username: ")

connection.close()
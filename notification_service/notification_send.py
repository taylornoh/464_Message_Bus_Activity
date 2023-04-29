#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

message_in = input("Send a notification: ")
while(message_in != "exit"):
    
    channel.queue_declare(queue='x->order')

    channel.basic_publish(exchange='', routing_key='x->order', body=message_in)
    print(" [x] Sent " + message_in)
    channel = connection.channel()


    # also send to user service
    channel.queue_declare(queue='x->user')

    channel.basic_publish(exchange='', routing_key='x->user', body=message_in)
    print(" [x] Sent " + message_in)

    message_in = input("Send a notification: ")

connection.close()
#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

message_in = input("Is the item avalible and what is the price? ")
while(message_in != "exit"):
    
    channel.queue_declare(queue='product->cart')

    channel.basic_publish(exchange='', routing_key='product->cart', body=message_in)
    print(" [x] Sent " + message_in)

    message_in = input("Is the item avalible and what is the price? ")

connection.close()
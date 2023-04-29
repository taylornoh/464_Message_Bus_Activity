import pika
import json

# establish a connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# create a queue named 'cart'
channel.queue_declare(queue='cart')

# define a message to be sent to the 'cart' queue
message = {
    'user_id': '1234',
    'product_id': '5678',
    'quantity': 2
}
message_body = json.dumps(message)

# publish the message to the 'cart' queue
channel.basic_publish(
    exchange='',
    routing_key='cart',
    body=message_body
)

# define a callback function to receive messages from the 'cart' queue
def callback(ch, method, properties, body):
    message = json.loads(body)
    print("Received message: {}".format(message))

# set up a consumer to receive messages from the 'cart' queue
channel.basic_consume(
    queue='cart',
    on_message_callback=callback,
    auto_ack=True
)

# start consuming messages from the 'cart' queue
print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
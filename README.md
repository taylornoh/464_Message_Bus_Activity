# 464_Message_Bus_Activity

# Names: AJ Albrecht & Taylor Noh

This project involves working in groups of 2-3 people to come up with an idea for a microservices architecture, and then implementing a message bus using RabbitMQ (or Kafka). The goal is to improve communication of views and collaborate on the architecture as a team.

Each group is responsible for coming up with at least 6 services for their idea, and determining the type of messages they will exchange. They will then implement the message bus using RabbitMQ (or Kafka), using the appropriate client libraries to publish and consume messages from the message bus.

This project provides an opportunity for students to work in groups and practice their programming and software development skills, while also gaining experience with microservices architecture and message bus technologies.

The program is a simple e-commerce system that allows customers to place orders and track their order history.

Reference: https://www.rabbitmq.com/tutorials/tutorial-one-python.html

User Service - responsible for managing user authentication and authorization
Product Service - responsible for managing the product catalog and inventory
Cart Service - responsible for managing the user's shopping cart
Order Service - responsible for managing orders and order history
Notification Service - responsible for sending notifications to customers regarding their orders or other events
Payment Service - responsible for managing payment processing for orders

What services will be communicating:

User Service sends messages to Product Service about user details and authorization. (user->product)
Product Service sends messages to Cart Service about product availability and pricing. (product->cart)
Cart Service sends messages to Order Service about the user's cart and order details. (catr->order)
Order Service sends messages to User Service and Notification Service about order completion. (order->notification and user)
Payment Service sends messages to Order Service about payment status.
(payment->order)
Notification Service sends messages to User Service and Order Service about notification details. (notification->user and order)

# To Run:

1. Navigate to the directory where your desired service python file is
2. Run "python <service>.py
3. On a separate terminal, navigate to the corresponding service's directory
4. Run "python <other-service.py"

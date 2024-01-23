#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import pika
import msgpack

class hr_pub_node(Node):
    
        def __init__(self):
            super().__init__('hr_pub')
            self.hr_publisher = self.create_publisher(Int32, '/hr', 10)
            self.get_logger().info("hr publisher node started")
            self.exchange = 'BioHarnessSummaryData'
            self.routing_key = ''
            self.receive_message()

        def receive_message(self):
            connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
            channel = connection.channel()
            channel.exchange_declare(exchange=self.exchange, exchange_type='fanout')
            queue_name = channel.queue_declare(queue='').method.queue
            channel.queue_bind(exchange=self.exchange, queue=queue_name, routing_key=self.routing_key)


            def callback(ch, method, properties, body):
                body_unpacked = msgpack.unpackb(body, raw=False)
                hr = body_unpacked['heartRate']
                msg = Int32()
                msg.data = hr
                # print(hr)
                self.hr_publisher.publish(msg)


            channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
            channel.start_consuming()  

def main(args=None):
    rclpy.init(args=args)
    node = hr_pub_node()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()



#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from std_msgs.msg import String
from std_msgs.msg import Float32

class hr_node(Node):
    def __init__(self, resting_hr=60, age=26):
        super().__init__("hr_node")
        self.hr_sub = self.create_subscription(Int32, "/hr", self.callback_hr, 10)
        self.command_pub = self.create_publisher(String, "/command", 10)
        self.parameter_pub = self.create_publisher(Float32, "/parameter", 10)

        self.resting_hr = resting_hr
        self.age =  age
        self.max_hr = 220 - self.age
        self.counter = 0

        
    
    def callback_hr(self, msg):
        self.get_logger().info("HR: " + str(msg.data))
        if msg.data < self.resting_hr:
            self.get_logger().info("Resting HR: " + str(msg.data))
            self.resting_hr = msg.data
            self.mets = 1
        elif msg.data > self.max_hr:
            self.get_logger().info("Max HR: " + str(msg.data))
            self.max_hr = msg.data
            self.mets = 100/3.5
            
        else:
            # self.get_logger().info("Normal HR: " + str(msg.data))
            self.mets = ((msg.data - self.resting_hr) / (self.max_hr - self.resting_hr)) * (100/3.5)

        if self.mets == 5:
            self.command_pub.publish(String(data="takeoff"))
            print("takeoff")
            self.counter = 1
        elif self.mets == 7:
            self.command_pub.publish(String(data="formation"))
            print("formation")
        elif self.mets == 2 and self.counter == 1:
            self.command_pub.publish(String(data="land"))
            print("land")
        self.parameter_pub.publish(Float32(data=self.mets))
        print(self.mets)



def main(args=None):
    rclpy.init(args=args)
    node = hr_node()
    rclpy.spin(node)
    rclpy.shutdown()



if __name__ == "__main__":
    main()
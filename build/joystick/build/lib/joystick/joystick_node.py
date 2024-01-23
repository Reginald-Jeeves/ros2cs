#!/usr/bin/env python3


import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from std_msgs.msg import Float32
from std_msgs.msg import String

class JoystickNode(Node):
    
    def __init__(self):
        super().__init__("joystick_node")    
        self.commands = []
        self.joy_subscriber = self.create_subscription(Joy,"/joy",self.joy_callback,10)
        self.command_publisher = self.create_publisher(String,"/command",10)
        self.parameter_publisher = self.create_publisher(Float32,"/parameter",10)
        

    def joy_callback(self, msg):
        self.get_logger().info(str(msg))
        if msg.buttons[0]==1:
            if len(self.commands) == 0 or self.commands[-1] != "takeoff":
                self.commands.append("takeoff")
                print(self.commands)
                self.get_logger().info("Takeoff")
                command = String()
                command.data = "takeoff"
                self.command_publisher.publish(command)
            self.get_logger().info("Takeoff")   
        elif msg.buttons[2]==1:
            if len(self.commands) == 0 or self.commands[-1] != "land":
                self.commands.append("land")
                self.get_logger().info("Land")
                command = String()
                command.data = "land"
                self.command_publisher.publish(command)
        elif msg.buttons[3]==1:
            if len(self.commands) == 0 or self.commands[-1] != "formation":
                self.commands.append("formation")
                self.get_logger().info("Formation")
                command = String()
                command.data = "formation"
                self.command_publisher.publish(command)
        elif msg.buttons[1]==1:
            if len(self.commands) == 0 or self.commands[-1] != "emergency":
                self.commands.append("emergency")
                self.get_logger().info("Emergency")
                command = String()
                command.data = "emergency"
                self.command_publisher.publish(command)
        if len(self.commands) > 5:
            self.commands.pop(0)

        
        parameter = Float32()
        parameter.data = msg.axes[1]
        self.parameter_publisher.publish(parameter)
        


def main(args=None):
    rclpy.init(args=args)
    node=JoystickNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()



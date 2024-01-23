
import rclpy
from rclpy.node import Node
from hsi_interfaces.msg import Gesture
from std_msgs.msg import String
from std_msgs.msg import Float32

class Gesture_pub_node(Node):
    
    def __init__(self):
        super().__init__("joystick_pub_node")
        self.gesture_subscriber = self.create_subscription(Gesture,"/gesture",self.ges_callback,10)
        self.command_publisher = self.create_publisher(String,"/command",10)
        self.parameter_publisher = self.create_publisher(Float32,"/parameter",10)
        self.commands = []

    def ges_callback(self, msg):
        if msg.gesture==1:
            if len(self.commands) == 0 or self.commands[-1] != "takeoff":
                self.commands.append("takeoff")
                print(self.commands)
                command = String()
                command.data = "takeoff"
                self.command_publisher.publish(command)  
        elif msg.gesture==2:
            if len(self.commands) == 0 or self.commands[-1] != "land":
                self.commands.append("land")
                command = String()
                command.data = "land"
                self.command_publisher.publish(command)
        elif msg.gesture==3:
            if len(self.commands) == 0 or self.commands[-1] != "formation":
                self.commands.append("formation")
                command = String()
                command.data = "formation"
                self.command_publisher.publish(command)

        radius = Float32()
        radius.data = self.distance_scaler(msg.distance_hands)
        self.parameter_publisher.publish(radius)
        
        if len(self.commands) > 5:
                self.commands = self.commands[-5:]


    def distance_scaler(self, distance):
        # distance is a float between 0 and 1
        # radius is a float between -1 and 1
        # formula to scale from 0 to 1 to -1 to 1 is (x - 0.5)*2
        radius = round((distance - 0.5)*2.0, 3)
        return radius

        
def main(args=None):
    rclpy.init(args=args)
    node=Gesture_pub_node()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()

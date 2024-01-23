from crazyflie_py import Crazyswarm
import numpy as np
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_msgs.msg import Float32
from geometry_msgs.msg import PoseStamped

class cf_phy_node(Node):
    def __init__(self, allcfs, timeHelper, Z):
        super().__init__("cf_trial_node")
        self.allcfs = allcfs
        self.timeHelper = timeHelper
        self.Z = Z
        self.cmd_subscriber = self.create_subscription(String,"/command",self.cf_cmd_callback,10)



    def cf_cmd_callback(self,msg):
        if msg.data == "takeoff":
            self.allcfs.takeoff(targetHeight=self.Z, duration=1.0)
            self.timeHelper.sleep(3.0)
            self.toff = True
        elif msg.data == "land":
            self.allcfs.land(targetHeight=0.02, duration=1.0)
            self.toff = False
        elif msg.data == "formation":
            pass
        elif msg.data == "emergency":
            self.allcfs.emergency()
            self.timeHelper.sleep(1.0)
         

def main():
    Z = 0.4
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs
    for cf in allcfs.crazyfliesById:
        print(cf)
    node = cf_phy_node(allcfs, timeHelper, Z)
    rclpy.spin(node)
    rclpy.shutdown()
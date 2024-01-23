#!/usr/bin/env python3

from crazyflie_py import Crazyswarm
import numpy as np
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_msgs.msg import Float32

class cfnode(Node):

    def __init__(self, allcfs, timeHelper):
        super().__init__("cf_node")    
        self.id = 0
        self.cmd_subscriber = self.create_subscription(String,"/command",self.cf_cmd_callback,10)
        self.allcfs = allcfs
        self.timeHelper = timeHelper
        self.toff = False
        self.rad_range = 0
        self.par_subscriber = self.create_subscription(Float32, "/parameter", self.cf_par_callback, 10)
    
    def cf_cmd_callback(self, msg):
        cf1 = self.allcfs.crazyflies[0]
        cf2 = self.allcfs.crazyflies[1]
        cf3 = self.allcfs.crazyflies[2]
        cf4 = self.allcfs.crazyflies[3]
        all = self.allcfs
        if msg.data == "takeoff":
            all.takeoff(targetHeight=1.0, duration=1.0)
            self.toff = True
            self.timeHelper.sleep(3.0)
        elif msg.data == "land":
            all.land(targetHeight=0.02, duration=1.0)
            self.toff = False
            #self.timeHelper.sleep(1.0)
        elif msg.data == "formation":
            print("Formation")
            cf1.goTo(np.array([-0.5, -0.5, 1.0]), 0.0, 2.0)
            cf2.goTo(np.array([1.5, -0.5, 1.0]), 0.0, 2.0)
            cf3.goTo(np.array([-0.5, 1.5, 1.0]), 0.0, 2.0)
            cf4.goTo(np.array([1.5, 1.5, 1.0]), 0.0, 2.0)
            self.timeHelper.sleep(3.0)
            cf1.goTo(np.array([0.0, 0.0, 1.0]), 0.0, 2.0)
            cf2.goTo(np.array([1.0, 0.0, 1.0]), 0.0, 2.0)
            cf3.goTo(np.array([0.0, 1.0, 1.0]), 0.0, 2.0)
            cf4.goTo(np.array([1.0, 1.0, 1.0]), 0.0, 2.0)

        elif msg.data == "emergency":
            all.emergency()

    def cf_par_callback(self, msg):
        cf1 = self.allcfs.crazyflies[0]
        cf2 = self.allcfs.crazyflies[1]
        cf3 = self.allcfs.crazyflies[2]
        cf4 = self.allcfs.crazyflies[3]
        all = self.allcfs
        #radius = 0.3 * msg.data


            
        if abs(msg.data) >= 0.3 and abs(msg.data)< 0.5 and self.toff == True and self.rad_range !=2:
            radius = np.sign(msg.data)* 0.4
            cf1.goTo(np.array(cf1.initialPosition) + np.array([-radius,-radius, 1.0]), 0.0, 2.0)
            cf2.goTo(np.array(cf2.initialPosition) + np.array([radius,-radius, 1.0]), 0.0, 2.0)
            cf3.goTo(np.array(cf3.initialPosition) + np.array([-radius,radius, 1.0]), 0.0, 2.0)
            cf4.goTo(np.array(cf4.initialPosition) + np.array([radius,radius, 1.0]), 0.0, 2.0)
            self.rad_range = 2
            self.timeHelper.sleep(1.0)

        elif abs(msg.data) >= 0.5 and abs(msg.data)< 0.7 and self.toff == True and self.rad_range !=3:
            radius = np.sign(msg.data)*0.6
            cf1.goTo(np.array(cf1.initialPosition) + np.array([-radius,-radius, 1.0]), 0.0, 2.0)
            cf2.goTo(np.array(cf2.initialPosition) + np.array([radius,-radius, 1.0]), 0.0, 2.0)
            cf3.goTo(np.array(cf3.initialPosition) + np.array([-radius,radius, 1.0]), 0.0, 2.0)
            cf4.goTo(np.array(cf4.initialPosition) + np.array([radius,radius, 1.0]), 0.0, 2.0)
            self.rad_range = 3
            self.timeHelper.sleep(1.0)

        
        elif abs(msg.data) >= 0.5 and abs(msg.data)< 0.7 and self.toff == True and self.rad_range !=4:
            radius = np.sign(msg.data)*0.9
            cf1.goTo(np.array(cf1.initialPosition) + np.array([-radius,-radius, 1.0]), 0.0, 2.0)
            cf2.goTo(np.array(cf2.initialPosition) + np.array([radius,-radius, 1.0]), 0.0, 2.0)
            cf3.goTo(np.array(cf3.initialPosition) + np.array([-radius,radius, 1.0]), 0.0, 2.0)
            cf4.goTo(np.array(cf4.initialPosition) + np.array([radius,radius, 1.0]), 0.0, 2.0)
            self.rad_range = 4
            self.timeHelper.sleep(1.0)



def main():
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs
    # rclpy.init()
    node = cfnode(allcfs, timeHelper)
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
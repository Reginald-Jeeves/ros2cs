#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
import numpy as np
from crazyflie_py import Crazyswarm
import math

class cf_pose(Node):

    def __init__(self, allcfs, timeHelper, Z):
        super().__init__('cf_pose')
        self.pose = np.zeros((4,3))
        self.num_cfs = 4
        self.allcfs = allcfs
        self.timeHelper = timeHelper
        self.Z = Z
        self.cf1_pose_subscriber = self.create_subscription(PoseStamped, '/cf1/pose', self.cf1_pose_callback, 10)
        self.cf2_pose_subscriber = self.create_subscription(PoseStamped, '/cf2/pose', self.cf2_pose_callback, 10)
        self.cf3_pose_subscriber = self.create_subscription(PoseStamped, '/cf3/pose', self.cf3_pose_callback, 10)
        self.cf4_pose_subscriber = self.create_subscription(PoseStamped, '/cf4/pose', self.cf4_pose_callback, 10)
        self._timer = self.create_timer(1.0, self.pose_printer)
        self.__agg_timer = self.create_timer(2.0, self.aggregate)
        #self.allcfs.land(targetHeight=0.02, duration=2.0)
       

    def cf1_pose_callback(self, msg):

        cf1_pose = np.array([msg.pose.position.x, msg.pose.position.y, msg.pose.position.z])
        self.pose[0] = cf1_pose
        #print(cf1_pose)

    def cf2_pose_callback(self, msg):

        cf2_pose = np.array([msg.pose.position.x, msg.pose.position.y, msg.pose.position.z])
        self.pose[1] = cf2_pose
        #print(cf2_pose)

    def cf3_pose_callback(self, msg):

        cf3_pose = np.array([msg.pose.position.x, msg.pose.position.y, msg.pose.position.z])
        self.pose[2] = cf3_pose
        #print(cf3_pose)

    def cf4_pose_callback(self, msg):

        cf4_pose = np.array([msg.pose.position.x, msg.pose.position.y, msg.pose.position.z])
        self.pose[3] = cf4_pose
        #print(cf4_pose)

    def pose_printer(self):
        print('The pose of all the drones is ' + str(self.pose))
        self.centroid_calc()
        self.cent_dist_calc()
    
    def centroid_calc(self):
        pose_sum = np.zeros(3)
        #print(self.pose)
        for num_cf in range(self.num_cfs):
            pose_sum = pose_sum + self.pose[num_cf]
        centroid = np.divide(pose_sum,self.num_cfs)
        #print(centroid)
        return centroid


    def cent_dist_calc(self):
        cent_norm = []
        cent_vec = []
        cent_hat = []
        for i,cf in enumerate(self.allcfs.crazyflies):
            cent_vec.append(self.centroid_calc() - self.pose[i])
            cent_norm.append(np.linalg.norm(cent_vec[i]))
            cent_hat.append(np.divide(cent_vec[i],cent_norm[i]))
        cent_norm = np.array(cent_norm)
        cent_vec = np.array(cent_vec)
        cent_hat = np.array(cent_hat)   
        #cent_hat = cent_vec / cent_norm[:,None]
        #print('centroid vectors are' + str(cent_vec))
        print('centroid norms are' + str(cent_norm))
        print('centroid hats are' + str(cent_hat))

        return cent_vec, cent_norm, cent_hat
    

    def aggregate(self):
        cent_vec, cent_norm, cent_hat = self.cent_dist_calc()
        for i,cf in enumerate(self.allcfs.crazyflies):
            goal = self.pose[i] + cent_hat[i]*0.3
            goal = np.array([goal[0], goal[1], 1.0])
            if not math.isnan(goal[0]):
                print('going to goal ' + str(goal))
                cf.goTo(goal, 0.0, 2.0)

        
        self.timeHelper.sleep(2.0)

        

def main():
    Z = 1.0
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs
    allcfs.takeoff(targetHeight=Z, duration=2.0)
    timeHelper.sleep(4.0)
    node = cf_pose(allcfs, timeHelper, Z)
    rclpy.spin(node)
    rclpy.shutdown()


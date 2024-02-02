#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
import numpy as np
from crazyflie_py import Crazyswarm
import math
from std_msgs.msg import String
from std_msgs.msg import Float32 

class cf_pose(Node):

    def __init__(self, allcfs, timeHelper, Z):
        super().__init__('cf_pose')
        self.pose = np.zeros((4,3))
        self.num_cfs = 4
        self.allcfs = allcfs
        self.timeHelper = timeHelper
        self.Z = Z
        # self.prev_par = 0.0
        # self.current_par = 0.0
        # self.delta = self.current_par - self.prev_par
        self.joystick_ip = 0.0
        self.toff = False
        self.cent_vec = np.array([]) # 2D Array of dimension 4x3 with each row the vector towards the centroid
        self.cent_norm =np.array([]) # 1D Array with distances between the drone and the centroid dimension is 1x4
        self.cent_hat = np.array([]) # 2D Array with unit vector of drones from the centroid dimension is 4x3
        self.centroid = 0 # Center of mass of the drones 1x3
        self.cf1_pose_subscriber = self.create_subscription(PoseStamped, '/cf1/pose', self.cf1_pose_callback, 10)
        self.cf2_pose_subscriber = self.create_subscription(PoseStamped, '/cf2/pose', self.cf2_pose_callback, 10)
        self.cf3_pose_subscriber = self.create_subscription(PoseStamped, '/cf3/pose', self.cf3_pose_callback, 10)
        self.cf4_pose_subscriber = self.create_subscription(PoseStamped, '/cf4/pose', self.cf4_pose_callback, 10)
        self.par_subscriber = self.create_subscription(Float32, "/parameter", self.cf_par_callback, 10)
        self.cmd_subscriber = self.create_subscription(String,"/command",self.cf_cmd_callback,10)
        self._timer = self.create_timer(1.0, self.pose_printer)
        self.__agg_timer = self.create_timer(1.0, self.aggregate)
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

    def cf_par_callback(self,msg):
        self.joystick_ip = round(msg.data, 1)

    def pose_printer(self):
        print('The pose of all the drones is ' + str(self.pose))
        self.centroid_calc()
        self.cent_dist_calc()
    
    def centroid_calc(self):
        pose_sum = np.zeros(3)
        #print(self.pose)
        for num_cf in range(self.num_cfs):
            pose_sum = pose_sum + self.pose[num_cf]
        self.centroid = np.divide(pose_sum,self.num_cfs)
        return self.centroid

    def cent_dist_calc(self):
        cent_norm = []
        cent_vec = []
        cent_hat = []
        for i,cf in enumerate(self.allcfs.crazyflies):
            cent_vec.append(np.subtract(self.centroid_calc(),self.pose[i]))
            cent_norm.append(np.linalg.norm(cent_vec[i]))
            cent_hat.append(np.divide(cent_vec[i],cent_norm[i]))
        cent_norm = np.array(cent_norm)
        cent_vec = np.array(cent_vec)
        cent_hat = np.array(cent_hat)     
        #cent_hat = cent_vec / cent_norm[:,None]
        #print('centroid vectors are' + str(self.cent_vec))
        #print('centroid norms are' + str(self.cent_norm))
        #print('centroid hats are' + str(self.cent_hat))
        return cent_vec, cent_norm, cent_hat
    
    def movement_dist_calc(self, cf_id):
        print("Joystick ip is " + str(self.joystick_ip))
        # print("Previous parameter is " + str(self.prev_par))
        # self.delta = self.current_par - self.prev_par
        # self.prev_par = self.current_par

        # joystick values: -1 to 1
        # delta max val

        # logic:
        # find centroid
        centroid = self.centroid_calc()
        print("Centroid is " + str(centroid))
        # find current position of ronde
        print("Current position is " + str(self.pose))
        # find norm
        vecs, norms, hats = self.cent_dist_calc()
        print('centroid vectors are' + str(vecs))
        print('centroid norms are' + str(norms))
        print('centroid hats are' + str(hats))

        norm_cf = norms[cf_id]
        print("Norm is " + str(norm_cf))
        # if (norm is <= 0.2) and (joystick ip negative or zero) then stay there
        if (norm_cf <= 0.2) and (self.joystick_ip <= 0.0):
            print("Staying put")
            movement_dist = 0.0
        
        # if (norm is <= 0.2) and (joystick ip positive) then move to (joystick * (scaled value))
        elif (norm_cf <= 0.2) and (self.joystick_ip > 0.0):
            print("Moving to joystick scaled value")
            movement_dist = self.joystick_ip * 0.8

        # if (norm is > 0.2 and norm < 1.0) then move to (joystick * (scaled value))
        elif (norm_cf > 0.2) and (norm_cf < 1.0):
            print("Moving to joystick scaled value")
            movement_dist = self.joystick_ip * 0.8
       
        # if (norm is >= 1.0) and (joystick ip positive or zero) then stay there
        elif (norm_cf >= 1.0) and (self.joystick_ip >= 0.0):
            print("Staying put")
            movement_dist = 0.0

        # if (norm is >= 1.0) and (joystick ip negative) then move to (joystick * (scaled value))
        elif (norm_cf >= 1.0) and (self.joystick_ip < 0.0):
            print("Moving to joystick scaled value")
            movement_dist = self.joystick_ip * 0.8

        # if norm+movement_dist < 0.2 return 0.2
        if norm_cf+movement_dist < 0.2:
            movement_dist = 0.2 - norm_cf
        # else if norm+movement > 1.0 return 1.0
        elif norm_cf+movement_dist > 1.0:
            movement_dist = 1.0 - norm_cf
        # else return norm+movement_dist
        else:
            movement_dist = movement_dist

        return round(movement_dist, 2)



    def aggregate(self):
        print("entering aggregate")

        if self.toff == False:
            print("not taking off")
            return

        
        print("All crazyflies: ", self.allcfs.crazyflies)
        for i,cf in enumerate(self.allcfs.crazyflies):
            movement_dist = self.movement_dist_calc(i)
            print("Movement distance is " + str(movement_dist))
            goal = self.pose[i] - self.cent_hat[i]*movement_dist
            goal = np.array([goal[0], goal[1], 1.0])
            cf.goTo(goal, 0.0, 1.0)


            # if movement_dist < 0:
            #     movement_dist = min(cent_norm[i]-0.2, abs(movement_dist))
            # #movement_dist = max(movement_dist, 0.0)
            # goal = self.pose[i] - cent_hat[i]*movement_dist
            # goal = np.array([goal[0], goal[1], 1.0])
            # if not math.isnan(goal[0]):
            #     print('going to goal ' + str(goal))
            #     speed = d/t, so 2.0 below, which is the time to move to goal, 
            #     needs to scale with d so that speed is the same
            #     cf.goTo(goal, 0.0, 1.0)

        # self.timeHelper.sleep(1.0)

def main():
    Z = 1.0
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs
    #allcfs.takeoff(targetHeight=Z, duration=2.0)
    timeHelper.sleep(4.0)
    node = cf_pose(allcfs, timeHelper, Z)
    rclpy.spin(node)
    rclpy.shutdown()

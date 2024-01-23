#!/usr/bin/env python3

from crazyflie_py import Crazyswarm
import numpy as np
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_msgs.msg import Float32

class cf_trial_node(Node):

    def __init__(self, allcfs, timeHelper, Z):
        super().__init__("cf_trial_node")
        self.allcfs = allcfs
        self.timeHelper = timeHelper
        self.Z = Z
        self.pose = []
        for cf in self.allcfs.crazyflies:
            self.pose.append(cf.initialPosition+ [0,0,self.Z])
        self.pose = np.array(self.pose)
        self.min_prox = 0.4
        self.increment = 0.2
        self.toff = False
        self.par_subscriber = self.create_subscription(Float32, "/parameter", self.cf_par_callback, 10)
        self.cmd_subscriber = self.create_subscription(String,"/command",self.cf_cmd_callback,10)
        self.latency_sim = 1.1 # DO NOT DECREASE BELOW 1.0, will cause irregular behaviour in cfs, increase to simulate latency
        self.timer_ = self.create_timer(2.0, self.aggregation)
        self.repulsion_scaling = 1
        self.repulsion_rad = 0.7
        


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
        if np.round(msg.data, 2) >= -1 and np.round(msg.data, 2) < -0.6:
            self.repulsion_rad = self.min_prox * self.repulsion_scaling
        elif np.round(msg.data, 2) >= -0.6 and np.round(msg.data, 2) < -0.2:
            self.repulsion_rad = 0.5 * self.repulsion_scaling
        elif np.round(msg.data, 2) >= -0.2 and np.round(msg.data, 2) < 0.2:
            self.repulsion_rad = 0.7 * self.repulsion_scaling
        elif np.round(msg.data, 2) >= 0.2 and np.round(msg.data, 2) < 0.6:
            self.repuslion_rad = 0.9 * self.repulsion_scaling
        elif np.round(msg.data, 2) >= 0.6 and np.round(msg.data, 2) < 1.0:
            self.repulsion_rad = 1.1 * self.repulsion_scaling

    def centroid_calc(self):
        sum = np.zeros(3)
        #print(self.pose)
        for num_cf,cf in enumerate(self.allcfs.crazyflies):
            sum = sum + self.pose[num_cf]
        centroid = np.divide(sum,num_cf+1)
        return(centroid)
    
    def cent_dist_calc(self):
        cent_norm = []
        cent_vec = []
        for i,cf in enumerate(self.allcfs.crazyflies):
            cent_vec.append(self.centroid_calc() - self.pose[i])
            cent_norm.append(np.linalg.norm(cent_vec[i]))
        cent_norm = np.array(cent_norm)
        cent_vec = np.array(cent_vec)
        cent_hat = cent_vec / cent_norm[:,None]
        return cent_vec, cent_norm, cent_hat
    
        #print(cent_vec)
        #print(cent_norm)
        #print(cent_hat)
    
    def aggregation(self):
        if self.toff == True:
            vector, norm, unit_vector = self.cent_dist_calc()
            for i,cf in enumerate(self.allcfs.crazyflies):
                conditional_distance = np.round(norm[i] - self.repulsion_rad,2)
                if conditional_distance == 0:
                    pass
                elif conditional_distance > 0:
                    #goal = self.pose[i] + self.tracking*self.increment*unit_vector[i]
                    goal = self.pose[i] + self.increment*unit_vector[i]
                    # Here the duration parameter allows to control how quickly the system reacts
                    # to the input, set to 1.0 to make the goto action to be executed in 1 second
                    cf.goTo(goal, 0.0, self.latency_sim)
                    self.pose[i] = goal
                    print(conditional_distance)
                elif conditional_distance < 0:
                    goal = self.pose[i] + conditional_distance*unit_vector[i]
                    cf.goTo(goal, 0.0, self.latency_sim)
                    self.pose[i] = goal
                    print(conditional_distance)
                
            

def main():
    Z = 1.0
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs
    #allcfs.takeoff(targetHeight=Z, duration=2.0)
    node = cf_trial_node(allcfs, timeHelper, Z)
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
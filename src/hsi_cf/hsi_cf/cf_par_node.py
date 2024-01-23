# In this script we find the topics pertaining to specific robots and we publish them as arrays
from crazyflie_py import Crazyswarm
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import Float32
import numpy as np


class cf_parameter_node(Node):

    def __init__(self, allcfs, timeHelper, Z):
        super().__init__("cf_parameter_node")
        self.pose = np.zeros((4,3))
        self.allcfs = allcfs
        self.timeHelper = timeHelper
        self.Z = Z
        self.subscription_cf1 = self.create_subscription(PoseStamped,"/cf1/pose",self.pose_callback_cf1,10)
        self.subscription_cf2 = self.create_subscription(PoseStamped,"/cf2/pose",self.pose_callback_cf2,10)
        self.subscription_cf3 = self.create_subscription(PoseStamped,"/cf3/pose",self.pose_callback_cf3,10)
        self.subscription_cf4 = self.create_subscription(PoseStamped,"/cf4/pose",self.pose_callback_cf4,10)
        self.subscription_par = self.create_subscription(Float32,"/parameter",self.pose_callback_cf4,10)
        self.increment = 0.2
        self.toff = True
        self.latency_sim = 1.1 # DO NOT DECREASE BELOW 1.0, will cause irregular behaviour in cfs, increase to simulate latency
        #self.timer_ = self.create_timer(1.5, self.aggregation)
        #self.repulsion_rad = 0.4
        self.min_prox = 0.4

    def pose_callback_cf1(self, msg):
        # self.get_logger().info("CF1: %s" % msg.pose.position.x)
        cf_pose = [msg.pose.position.x, msg.pose.position.y, msg.pose.position.z]
        self.pose[0] = cf_pose
        print(self.pose[0])

    def pose_callback_cf2(self, msg):
        # self.get_logger().info("CF2: %s" % msg.pose.position.x)
        cf_pose = [msg.pose.position.x, msg.pose.position.y, msg.pose.position.z]
        self.pose[1] = cf_pose
        print(self.pose[1])

    def pose_callback_cf3(self, msg):
        # self.get_logger().info("CF3: %s" % msg.pose.position.x)
        cf_pose = [msg.pose.position.x, msg.pose.position.y, msg.pose.position.z]
        self.pose[2] = cf_pose
        print(self.pose[2])

    def pose_callback_cf4(self, msg):
        # self.get_logger().info("CF4: %s" % msg.pose.position.x)
        cf_pose = [msg.pose.position.x, msg.pose.position.y, msg.pose.position.z]
        self.pose[3] = cf_pose
        print(self.pose[3])


    def cf_par_callback(self,msg):
        if np.round(msg.data, 2) >= -1 and np.round(msg.data, 2) < -0.6:
            self.repulsion_rad = self.min_prox
        elif np.round(msg.data, 2) >= -0.6 and np.round(msg.data, 2) < -0.2:
            self.repulsion_rad = 0.5
        elif np.round(msg.data, 2) >= -0.2 and np.round(msg.data, 2) < 0.2:
            self.repulsion_rad = 0.7
        elif np.round(msg.data, 2) >= 0.2 and np.round(msg.data, 2) < 0.6:
            self.repuslion_rad = 0.9
        elif np.round(msg.data, 2) >= 0.6 and np.round(msg.data, 2) < 1.0:
            self.repulsion_rad = 1.1

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
                    #self.pose[i] = goal
                    print(conditional_distance)
                elif conditional_distance < 0:
                    goal = self.pose[i] + conditional_distance*unit_vector[i]
                    cf.goTo(goal, 0.0, self.latency_sim)
                    #self.pose[i] = goal
                    print(conditional_distance)
                
            

        

def main():
    Z = 0.6
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs
    allcfs.takeoff(targetHeight=Z, duration=2.0)
    timeHelper.sleep(3.0)
    node = cf_parameter_node(allcfs,timeHelper, Z)
    rclpy.spin_once(node,timeout_sec=40)
    rclpy.shutdown()
    allcfs.land(targetHeight=0.02, duration=2.0)

if __name__ == '__main__':
    main()
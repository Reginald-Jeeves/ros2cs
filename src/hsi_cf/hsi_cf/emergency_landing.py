#!/usr/bin/env python

from crazyflie_py import Crazyswarm
import numpy as np
import rclpy
from rclpy.node import Node



def main():

    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs
    print('press any button for emergency landing...')
    swarm.input.waitUntilButtonPressed()
    allcfs.land(targetHeight=0.02, duration=1.0)
    allcfs.emergency()
    timeHelper.sleep(1.0)


if __name__ == '__main__':
    main()
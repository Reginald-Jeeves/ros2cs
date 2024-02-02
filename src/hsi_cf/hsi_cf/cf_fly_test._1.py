#!/usr/bin/env python

from pathlib import Path

from crazyflie_py import Crazyswarm
from crazyflie_py.uav_trajectory import Trajectory
import numpy as np


def main():
    Z = 1.0
    
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs
    for cf in allcfs.crazyfliesByName:
        print(cf)
    allcfs.takeoff(targetHeight=Z, duration=1.0+Z)
    timeHelper.sleep(8.0)
    
    
    pos1 = np.array(cf.initialPosition) + np.array([0.3, 0.0, 1.0])
    allcfs.goTo(pos1, 0, 2.0)
        

    print('press button to land')
    swarm.input.waitUntilButtonPressed()

    allcfs.land(targetHeight=0.02, duration=2.0)
    timeHelper.sleep(1.0+Z)

if __name__ == '__main__':
    main()

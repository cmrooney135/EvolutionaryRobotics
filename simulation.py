import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import constants as c
from world import WORLD
from robot import ROBOT
from sensor import SENSOR
class SIMULATION:
    def __init__(self):
        self.world = WORLD()
        self.robot = ROBOT()


    def Run(self):
        for i in range(c.size):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Act(i)
            print(f"iteration : {i}")

            time.sleep(c.sleeptime)

def __del__(self):
    p.disconnect()

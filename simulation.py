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
    def __init__(self, directOrGUI):
        if directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)

        print(f"Simulation running in {directOrGUI} mode")
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
        p.setGravity(0, 0, c.gravZ, self.physicsClient)

        self.world = WORLD()
        self.robot = ROBOT()


    def Run(self):
        for i in range(c.size):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
            #print(f"iteration : {i}")

            time.sleep(c.sleeptime)
    def Get_Fitness(self):
        self.robot.Get_Fitness()

def __del__(self):
    p.disconnect()

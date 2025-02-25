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
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        self.world = WORLD()
        self.robot = ROBOT()

        p.setGravity(0, 0, c.gravZ, self.physicsClient)

        #pyrosim.Prepare_To_Simulate(self.robot.robotID)
    def Run(self):
        for i in range(c.size):
            p.stepSimulation()
            self.robot.Sense(i)
            '''
            c.backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("backLeg")
            print(i)
            print("backleg sensor val: ")
            print(c.backLegSensorValues[i])
            c.frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("frontLeg")

            pyrosim.Set_Motor_For_Joint(
                bodyIndex=self.robot.robotID,
                jointName=b"torso_backLeg",
                controlMode=p.POSITION_CONTROL,
                targetPosition=-c.backleg_motor_targ,
                maxForce=c.maxforce)
            pyrosim.Set_Motor_For_Joint(
                bodyIndex=self.robot.robotID,
                jointName=b"torso_frontLeg",
                controlMode=p.POSITION_CONTROL,
                targetPosition=c.frontleg_motor_targ,
                maxForce=c.maxforce)'''
            #print(i)

            time.sleep(c.sleeptime)

def __del__(self):
    p.disconnect()


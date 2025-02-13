import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import random as rand


amplitude_frontleg = 1
frequency_frontleg = 100 * np.pi
phaseOffset_frontleg = np.pi/4

amplitude_backleg = 2
frequency_backleg = -100 * np.pi /4
phaseOffset_backleg = 0

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-10, physicsClient)

planeId = p.loadURDF("plane.urdf")
robotID = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotID)
backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)

targetAngles_frontleg = np.sin(np.linspace(-1. ,1. , 1000))
targetAngles_frontleg = targetAngles_frontleg * (np.pi / 4)
motorControl_frontleg = np.zeros(1000)
targetAngles_backleg = np.sin(np.linspace(-1. ,1. , 1000))
targetAngles_backleg = targetAngles_backleg * (np.pi / 4)
motorControl_backleg = np.zeros(1000)
for i in range (1000):
    motorControl_frontleg[i] = amplitude_frontleg * np.sin(frequency_frontleg * targetAngles_frontleg[i] + phaseOffset_frontleg)
    motorControl_backleg[i] = amplitude_backleg * np.sin(frequency_backleg * targetAngles_backleg[i] + phaseOffset_backleg)


#np.save("data/motorControlfront.npy", motorControl_frontleg)
#np.save("data/motorControlback.npy", motorControl_backleg)


#exit()

for i in range (1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("backLeg")
    print(i)
    print("backleg sensor val: ")
    print(backLegSensorValues[i])
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("frontLeg")

    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotID,
        jointName=b"torso_backLeg",
        controlMode=p.POSITION_CONTROL,
        targetPosition=-np.pi/3,
        maxForce=50)
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotID,
        jointName=b"torso_frontLeg",
        controlMode=p.POSITION_CONTROL,
        targetPosition=np.pi/3,
        maxForce=50)

    time.sleep(0.0004)


p.disconnect()
np.save("data/back_leg_sensor_values.npy", backLegSensorValues)
np.save("data/front_leg_sensor_values.npy", frontLegSensorValues)

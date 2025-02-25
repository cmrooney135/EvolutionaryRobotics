'''
import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import constants as c

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,c.gravZ, physicsClient)

planeId = p.loadURDF("plane.urdf")
robotID = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotID)
backLegSensorValues = np.zeros(c.size)
frontLegSensorValues = np.zeros(c.size)


for i in range (c.size):
    c.motorControl_frontleg[i] = c.amplitude_frontleg * np.sin(c.frequency_frontleg * c.targetAngles_frontleg[i] + c.phaseOffset_frontleg)
    c.motorControl_backleg[i] = c.amplitude_backleg * np.sin(c.frequency_backleg * c.targetAngles_backleg[i] + c.phaseOffset_backleg)


for i in range (c.size):
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
        targetPosition=-c.backleg_motor_targ,
        maxForce=c.maxforce)
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotID,
        jointName=b"torso_frontLeg",
        controlMode=p.POSITION_CONTROL,
        targetPosition=c.frontleg_motor_targ,
        maxForce=c.maxforce)

    time.sleep(c.sleeptime)


p.disconnect()
np.save("data/back_leg_sensor_values.npy", backLegSensorValues)
np.save("data/front_leg_sensor_values.npy", frontLegSensorValues)
'''
from simulation import SIMULATION

simulation = SIMULATION()
simulation.Run()
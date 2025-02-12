import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import random as rand



physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-10, physicsClient)

planeId = p.loadURDF("plane.urdf")
robotID = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotID)
backLegSensorValues = np.zeros(100)
frontLegSensorValues = np.zeros(100)

targetAngles = np.linspace(0,2*np.pi, 100)
np.save("data/targetAngles.npy", targetAngles)
exit()


for i in range (100):
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
        targetPosition=(rand.random() * np.pi) - (np.pi / 2),
        maxForce=50)
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotID,
        jointName=b"torso_frontLeg",
        controlMode=p.POSITION_CONTROL,
        targetPosition=(rand.random() * np.pi) - (np.pi / 2),
        maxForce=50)

    time.sleep(0.004)


p.disconnect()
np.save("data/back_leg_sensor_values.npy", backLegSensorValues)
np.save("data/front_leg_sensor_values.npy", frontLegSensorValues)

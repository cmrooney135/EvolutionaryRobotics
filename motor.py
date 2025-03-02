import pyrosim.pyrosim as pyrosim
import numpy as np
import constants as c
import pybullet as p

class MOTOR:
    def __init__(self, jointName):
        self.offset = None
        self.frequency = None
        self.amplitude = None
        self.jointName = jointName
        self.motorValues = np.zeros(c.size)
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude = c.amplitude
        if(self.jointName == b"torso_frontLeg"):
            self.frequency = c.frequency
        else:
            self.frequency = c.frequency /2


        self.offset = c.phaseOffset
        self.time_steps = np.linspace(0, 2 * np.pi, c.size)
        self.motorValues = self.amplitude * np.sin(self.frequency * self.time_steps + self.offset)

    def Set_Value(self, robot, t):

        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robot.robotID,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=self.motorValues[t],
            maxForce=c.maxforce)

    def Save_Values(self):
        np.save(f"data/motors/{self.jointName}_values", self.motorValues)



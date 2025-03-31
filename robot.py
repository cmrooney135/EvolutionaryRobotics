import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import constants as c
from sensor import SENSOR
import os
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK


class ROBOT:
    def __init__(self, solutionID):
        self.robotID = p.loadURDF("body.urdf")
        self.sensors = {}
        self.motors = {}
        self.solutionID = solutionID
        brainFile = "brain" + str(solutionID) + ".nndf"  # NEW:
        self.nn = NEURAL_NETWORK(brainFile)


        pyrosim.Prepare_To_Simulate(self.robotID)
        os.system("rm " + brainFile)  # NEW:
        print(f"Brain file deleted: {brainFile}")

        self.Prepare_To_Sense()
        self.Prepare_to_Act()


    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            #print(linkName)
            self.sensors[linkName] = SENSOR(linkName)

    def Prepare_to_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Sense(self, t):
        for sensor in self.sensors.values():
            sensor.Get_Value(t)

    def Act(self, t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName).encode("utf-8")
                #print(f"Neuron name : {neuronName}" )
                if isinstance(jointName, str):
                    jointName = jointName.encode("utf-8")
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
                self.motors[jointName].Set_Value(self, desiredAngle)
                #print(f"desired angle : {desiredAngle}" )


    def Think(self):
        self.nn.Update()
        #self.nn.Print()

    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotID,0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]
        print(xCoordinateOfLinkZero)
        tmpFile = "tmp" + str(self.solutionID) + ".txt"  # NEW:
        fitnessFile = "fitness" + str(self.solutionID) + ".txt"  # NEW:
        with open(tmpFile, "w") as f:
            f.write(str(xCoordinateOfLinkZero))
        os.system("mv " + tmpFile + " " + fitnessFile)




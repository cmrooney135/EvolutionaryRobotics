import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import constants as c
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK


class ROBOT:
    def __init__(self):
        self.robotID = p.loadURDF("body.urdf")
        self.sensors = {}
        self.motors = {}
        self.nn = NEURAL_NETWORK("brain.nndf")


        pyrosim.Prepare_To_Simulate(self.robotID)

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
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                #print(f"robotID: ", self.robotID)
                #exit()
                #jointName = jointName.decode("utf-8")

                self.motors[jointName].Set_Value(self, desiredAngle)
        #for motor in self.motors.values():
         #   motor.Set_Value(self, t)

    def Think(self):
        self.nn.Update()
        #self.nn.Print()

    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotID,0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]
        print(xCoordinateOfLinkZero)
        f = open("fitness.txt", "w")
        f.write(str(xCoordinateOfLinkZero))
        f.close()




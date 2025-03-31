import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import time
import os
import constants as c
class SOLUTION:
    def __init__ (self, myID):
        self.weights = (np.random.rand(c.numSensorNeurons, c.numMotorNeurons)) * 2 - 1
        self.myID = myID

    def Set_ID(self, newID):  # NEW: Update the solution's unique ID.
        self.myID = newID

    def Evaluate(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        print(f"running simulate with {directOrGUI}")
        cmd = "python3 simulate.py " + directOrGUI + " " + str(self.myID) + " 2&>1 &"
        os.system(cmd)
        fitnessFile = "fitness" + str(self.myID) +".txt"
        while not os.path.exists(fitnessFile):
            time.sleep(0.01)
        f = open(fitnessFile, "r")
        self.fitness = float(f.read())
        print(self.fitness)
        f.close()
    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        print(f"running simulate with {directOrGUI}")
        cmd = "python simulate.py " + directOrGUI + " " + str(self.myID) + " &"  # NEW:
        os.system(cmd)

    def Wait_for_Simulation_to_End(self):
        fitnessFile = "fitness" + str(self.myID) + ".txt"  # NEW:
        #print(f"reading from fitness file {fitnessFile}")
        while not os.path.exists(fitnessFile):
            time.sleep(0.01)
        f = open(fitnessFile, "r")
        self.fitness = float(f.read())
        #print(self.fitness)
        f.close()
        #print("Solution", self.myID, "fitness:", self.fitness)  # NEW: For verification
        os.system("rm " + fitnessFile)  # NEW: Clean up the fitness file

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        # Torso
        pyrosim.Send_Cube(name="torso", pos=[0, 0, 1], size=[1, 1, 1])

        # BackLeg
        pyrosim.Send_Cube(name="backLeg", pos=[0, -0.5, 0], size=[0.2, 1, 0.2])

        # FrontLeg
        pyrosim.Send_Cube(name="frontLeg", pos=[0, 0.5, 0], size=[0.2, 1, 0.2])

        # LeftLeg
        pyrosim.Send_Cube(name="leftLeg", pos=[-0.5, 0, 0], size=[1, 0.2, 0.2])

        # RightLeg
        pyrosim.Send_Cube(name="rightLeg", pos=[0.5, 0, 0], size=[1, 0.2, 0.2])

        # FrontLowerLeg
        pyrosim.Send_Cube(name="frontLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        # BackLowerLeg
        pyrosim.Send_Cube(name="backLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        # LeftLowerLeg
        pyrosim.Send_Cube(name="leftLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        # RightLowerLeg
        pyrosim.Send_Cube(name="rightLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.Send_Joint(name="torso_backLeg", parent="torso", child="backLeg", type="revolute",
                           position=[0, -0.5, 1], jointAxis="1 0 0")
        pyrosim.Send_Joint(name="torso_frontLeg", parent="torso", child="frontLeg", type="revolute",
                           position=[0, 0.5, 1], jointAxis="1 0 0")
        pyrosim.Send_Joint(name="torso_leftLeg", parent="torso", child="leftLeg", type="revolute",
                           position=[-0.5, 0, 1], jointAxis="0 1 0")
        pyrosim.Send_Joint(name="torso_rightLeg", parent="torso", child="rightLeg", type="revolute",
                           position=[0.5, 0, 1], jointAxis="0 1 0")
        pyrosim.Send_Joint(name="frontLeg_frontLowerLeg", parent="frontLeg", child="frontLowerLeg", type="revolute",
                           position=[0, 1, 0], jointAxis="1 0 0")
        pyrosim.Send_Joint(name="backLeg_backLowerLeg", parent="backLeg", child="backLowerLeg", type="revolute",
                           position=[0, -1, 0], jointAxis="1 0 0")
        pyrosim.Send_Joint(name="leftLeg_leftLowerLeg", parent="leftLeg", child="leftLowerLeg", type="revolute",
                           position=[-1, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Joint(name="rightLeg_rightLowerLeg", parent="rightLeg", child="rightLowerLeg", type="revolute",
                           position=[1, 0, 0], jointAxis="0 1 0")

        pyrosim.End()

    def Create_Brain(self):
        brainFileName = "brain" + str(self.myID) + ".nndf"  # NEW: Use unique filename
        pyrosim.Start_NeuralNetwork(brainFileName)
        pyrosim.Send_Sensor_Neuron(name=0, linkName="torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="backLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="frontLeg")

        pyrosim.Send_Motor_Neuron(name=3, jointName="torso_backLeg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="torso_frontLeg")
        pyrosim.Send_Sensor_Neuron(name=5, linkName="frontLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=6, linkName="backLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=7, linkName="leftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=8, linkName="rightLowerLeg")

        pyrosim.Send_Motor_Neuron(name=9, jointName="torso_leftLeg")
        pyrosim.Send_Motor_Neuron(name=10, jointName="torso_rightLeg")
        pyrosim.Send_Motor_Neuron(name=11, jointName="frontLeg_frontLowerLeg")
        pyrosim.Send_Motor_Neuron(name=12, jointName="backLeg_backLowerLeg")
        pyrosim.Send_Motor_Neuron(name=13, jointName="leftLeg_leftLowerLeg")
        pyrosim.Send_Motor_Neuron(name=14, jointName="rightLeg_rightLowerLeg")


        for sensorNeuron in range(c.numSensorNeurons):
            for motorNeuron in range(c.numMotorNeurons):
                weight = self.weights[sensorNeuron][motorNeuron]
                pyrosim.Send_Synapse(sourceNeuronName=str(sensorNeuron), targetNeuronName=str(motorNeuron + c.numSensorNeurons), weight=weight)

        pyrosim.End()
    def Mutate(self):
        random_row = random.randint(0, c.numMotorNeurons)

        random_col = random.randint(0, 1)

        self.weights[random_row, random_col] = random.random() * 2 - 1

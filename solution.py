import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import time
import os
class SOLUTION:
    def __init__ (self, myID):
        self.weights = (np.random.rand(3, 2)) * 2 - 1
        self.myID = myID

    def Set_ID(self, newID):  # NEW: Update the solution's unique ID.
        self.myID = newID

    def Evaluate(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        print(f"running simulate with {directOrGUI}")
        cmd = "python simulate.py " + directOrGUI + " " + str(self.myID) + " &"  # NEW:
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
        pyrosim.Send_Cube(name="torso", pos=[1.5, 0, 1.5], size=[1, 1, 1])
        pyrosim.Send_Joint(name="torso_frontLeg", parent="torso", child="frontLeg",
                           type="revolute", position=[2, 0, 1])
        pyrosim.Send_Cube(name="frontLeg", pos=[.5, 0, -.5], size=[1, 1, 1])
        pyrosim.Send_Joint(name="torso_backLeg", parent="torso", child="backLeg",
                           type="revolute", position=[1, 0, 1])
        pyrosim.Send_Cube(name="backLeg", pos=[-0.5, 0, -0.5], size=[1, 1, 1])

        pyrosim.End()

    def Create_Brain(self):
        brainFileName = "brain" + str(self.myID) + ".nndf"  # NEW: Use unique filename
        pyrosim.Start_NeuralNetwork(brainFileName)
        row = [0, 1, 2]
        pyrosim.Send_Sensor_Neuron(name=0, linkName="torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="backLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="frontLeg")

        col = [3, 4]
        pyrosim.Send_Motor_Neuron(name=3, jointName="torso_backLeg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="torso_frontLeg")

        for currentRow in range(3):
            for currentColumn in range(2):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn + 3, weight=self.weights[currentRow][currentColumn])

        pyrosim.End()
    def Mutate(self):
        random_row = random.randint(0, 2)

        random_col = random.randint(0, 1)

        self.weights[random_row, random_col] = random.random() * 2 - 1

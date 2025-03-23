import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import os
class SOLUTION:
    def __init__ (self):
        self.weights = (np.random.rand(3, 2)) * 2 - 1

    def Evaluate(self, directOrGUI):
        print(f"running generate and simulate with {directOrGUI}")
        os.system("python3 generate.py")
        os.system("python simulate.py " + str(directOrGUI))


        f = open("fitness.txt", "r")
        self.fitness = float(f.read())
        print(self.fitness)
        f.close()

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
        pyrosim.Start_NeuralNetwork("brain.nndf")
        row = [0, 1, 2]
        pyrosim.Send_Sensor_Neuron(name=0, linkName="torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="backLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="frontLeg")

        col = [3, 4]
        pyrosim.Send_Motor_Neuron(name=3, jointName="torso_backLeg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="torso_frontLeg")

        for current_row in row:
            for current_col in col:
                pyrosim.Send_Synapse(sourceNeuronName=current_row, targetNeuronName=current_col + 3, weight=self.weights[current_row][current_col])

        pyrosim.End()
    def Mutate(self):
        random_row = random.randint(0, 2)

        random_col = random.randint(0, 1)

        self.weights[random_row, random_col] = random.random() * 2 - 1

import pyrosim.pyrosim as pyrosim

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.End()

def Generate_Body():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="torso", pos=[1.5, 0, 1.5], size=[1, 1, 1])
    pyrosim.Send_Joint(name="torso_frontLeg", parent="torso", child="frontLeg",
                       type="revolute", position=[2, 0, 1])
    pyrosim.Send_Cube(name="frontLeg", pos=[.5, 0, -.5], size=[1, 1, 1])
    pyrosim.Send_Joint(name="torso_backLeg", parent="torso", child="backLeg",
                       type="revolute", position=[1, 0, 1])
    pyrosim.Send_Cube(name="backLeg", pos=[-0.5, 0, -0.5], size=[1, 1, 1])

    pyrosim.End()

def Generate_Brain():
    pyrosim.Start_NeuralNetwork("brain.nndf")
    pyrosim.Send_Sensor_Neuron(name=0, linkName="torso")
    pyrosim.Send_Sensor_Neuron(name=1, linkName="backLeg")
    pyrosim.Send_Sensor_Neuron(name=2, linkName="frontLeg")
    pyrosim.Send_Motor_Neuron(name=3, jointName="torso_backLeg")
    pyrosim.Send_Motor_Neuron(name=4, jointName="torso_frontLeg")

    pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=3, weight=-3.0)
    pyrosim.Send_Synapse(sourceNeuronName=2, targetNeuronName=3, weight=-6.0)
    pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=2, weight=-2.0)
    pyrosim.Send_Synapse(sourceNeuronName=3, targetNeuronName=1, weight=-0.4)



    pyrosim.End()

def Create_Robot():
   pass
def main():
    Create_World()
    Generate_Body()
    Generate_Brain()


if __name__ == "__main__":
    main()
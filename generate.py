import pyrosim.pyrosim as pyrosim
import random
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
    sensor_neurons = [0, 1, 2]
    pyrosim.Send_Sensor_Neuron(name=0, linkName="torso")
    pyrosim.Send_Sensor_Neuron(name=1, linkName="backLeg")
    pyrosim.Send_Sensor_Neuron(name=2, linkName="frontLeg")

    motor_neurons = [3, 4]
    pyrosim.Send_Motor_Neuron(name=3, jointName="torso_backLeg")
    pyrosim.Send_Motor_Neuron(name=4, jointName="torso_frontLeg")

    for sensor in sensor_neurons:
        for motor in motor_neurons:
            pyrosim.Send_Synapse(sourceNeuronName=sensor, targetNeuronName=motor, weight=random.uniform(-1,1))

    pyrosim.End()

def Create_Robot():
   pass
def main():
    Create_World()
    Generate_Body()
    Generate_Brain()


if __name__ == "__main__":
    main()
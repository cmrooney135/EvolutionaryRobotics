import pyrosim.pyrosim as pyrosim

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.End()

def Genetate_Body():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="torso", pos=[1.5, 0, 1.5], size=[1, 1, 1])
    pyrosim.Send_Joint(name="torso_frontLeg", parent="torso", child="frontLeg",
                       type="revolute", position=[2, 0, 1])
    pyrosim.Send_Cube(name="frontLeg", pos=[.5, 0, -.5], size=[1, 1, 1])
    pyrosim.Send_Joint(name="torso_backLeg", parent="torso", child="backLeg",
                       type="revolute", position=[1, 0, 1])
    pyrosim.Send_Cube(name="backLeg", pos=[-0.5, 0, -0.5], size=[1, 1, 1])

    pyrosim.End()

def Create_Robot():
   pass
def main():
    Create_World()
    Genetate_Body()


if __name__ == "__main__":
    main()
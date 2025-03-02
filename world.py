from robot import ROBOT
import pybullet as p
import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import constants as c
class WORLD:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
        p.setGravity(0, 0, c.gravZ, self.physicsClient)

        self.planeId = p.loadURDF("plane.urdf")

        p.loadSDF("world.sdf")


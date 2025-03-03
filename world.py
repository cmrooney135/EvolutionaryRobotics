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
        p.loadSDF("world.sdf")
        self.planeId = p.loadURDF("plane.urdf")



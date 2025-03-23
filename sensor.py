import constants as c
import numpy as np
import pyrosim.pyrosim as pyrosim

class SENSOR:
    def __init__(self, linkname):
        self.linkName = linkname
        self.values = np.zeros(c.size)

    def Get_Value(self, t):
        self.t = t
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)


    def Save_Values(self):
        np.save(f"data/sensors/{self.linkName}_values", self.values)

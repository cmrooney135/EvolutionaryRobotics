import pyrosim.pyrosim as pyrosim

import constants as c


class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude = c.amplitude
        self.frequency = c.frequency
        self.offset = c.phaseOffset
        '''pyrosim.Set_Motor_For_Joint(
                    bodyIndex=robotID,
                    jointName=b"torso_backLeg",
                    controlMode=p.POSITION_CONTROL,
                    targetPosition=-c.backleg_motor_targ,
                    maxForce=c.maxforce)
                pyrosim.Set_Motor_For_Joint(
                    bodyIndex=robotID,
                    jointName=b"torso_frontLeg",
                    controlMode=p.POSITION_CONTROL,
                    targetPosition=c.frontleg_motor_targ,
                    maxForce=c.maxforce)'''

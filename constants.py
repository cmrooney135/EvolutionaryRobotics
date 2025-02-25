import numpy as np

amplitude_frontleg = 1
frequency_frontleg = 100 * np.pi
phaseOffset_frontleg = np.pi/4

amplitude = 1
frequency = 100 * np.pi
phaseOffset = np.pi/4

amplitude_backleg = 2
frequency_backleg = -100 * np.pi /4
phaseOffset_backleg = 0

pio4 = (np.pi / 4)
targetAngles_frontleg = np.sin(np.linspace(-1. ,1. , 1000))
targetAngles_frontleg = targetAngles_frontleg * pio4
motorControl_frontleg = np.zeros(1000)
targetAngles_backleg = np.sin(np.linspace(-1. ,1. , 1000))
targetAngles_backleg = targetAngles_backleg * pio4
motorControl_backleg = np.zeros(1000)

gravZ = -10


backleg_motor_targ = (np.pi / 3)
frontleg_motor_targ = (np.pi / 3)

sleeptime = 0.0004
maxforce = 50
size = 1000
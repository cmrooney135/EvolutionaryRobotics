import numpy as np
import matplotlib.pyplot as plt

#backLegSensorValues = np.load("data/back_leg_sensor_values.npy")
#frontLegSensorValues = np.load("data/front_leg_sensor_values.npy")
#targetAngles = np.load("data/motorControl.npy")
frontleg = np.load("data/motorControlfront.npy")
backleg = np.load("data/motorControlback.npy")



#plt.plot(backLegSensorValues, label="back Leg sensor values", linewidth=3)
#plt.plot(frontLegSensorValues, label="front Leg sensor values")
#plt.title("Back leg and front leg sensor values")
#plt.legend()
#plt.savefig("sensorvals.png", dpi=300, bbox_inches='tight')
#plt.show()

plt.plot(backleg, label="back Leg  values", linewidth=3)
plt.plot(frontleg, label="front Leg  values")
plt.title("leg Values")
plt.savefig("legs.png", dpi=300, bbox_inches='tight')
plt.show()
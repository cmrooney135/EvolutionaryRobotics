import numpy as np
import matplotlib.pyplot as plt

#backLegSensorValues = np.load("data/back_leg_sensor_values.npy")
#frontLegSensorValues = np.load("data/front_leg_sensor_values.npy")
targetAngles = np.load("data/targetAngles.npy")



#plt.plot(backLegSensorValues, label="back Leg sensor values", linewidth=3)
#plt.plot(frontLegSensorValues, label="front Leg sensor values")
#plt.title("Back leg and front leg sensor values")
#plt.legend()
#plt.savefig("plot.png", dpi=300, bbox_inches='tight')
#plt.show()

plt.plot(targetAngles, np.sin(targetAngles))
plt.title("sin Values")
plt.savefig("sinValues.png", dpi=300, bbox_inches='tight')
plt.show()
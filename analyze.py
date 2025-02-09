import numpy
import matplotlib.pyplot as plt
from Simulate import backLegSensorValues

backLegSensorValues = numpy.load(backLegSensorValues.npy)

plt.plot(backLegSensorValues)
plt.show()
import pybullet as p
import time
import pybullet_data

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-10, physicsClient)

planeId = p.loadURDF("plane.urdf")
robotID = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

for i in range (10000):
    p.stepSimulation()
    time.sleep(0.004)
    print(i)

p.disconnect()
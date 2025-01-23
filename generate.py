import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")
for j in range(5):
    for k in range(5):
        dim = 1

        for i in range (10):
            add = i + 0.5
            pyrosim.Send_Cube(name=f"Box_{j}_{k}_{i}", pos=[j, k, add], size=[dim, dim, dim])
            dim = dim * 0.9
pyrosim.End()

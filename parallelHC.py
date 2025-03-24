from solution import SOLUTION
import constants as c
import copy
import os
class PARALLEL_HILL_CLIMBER:
    def __init__ (self):
        self.parents = {}
        self.nextAvailableID = 0
        os.system("rm brain*.nndf")  # Use "del brain*.nndf" on Windows
        os.system("rm fitness*.txt")  # Use "del fitness*.txt" on Windows
        for i in range(c.populationSize):  # NEW:
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
        #self.parent = SOLUTION()

    def Evolve(self):
        # First, evaluate all parents in parallel using GUI mode.
        self.Evaluate(self.parents, "DIRECT")  # NEW:
        # Now evolve for a number of generations.
        for gen in range(c.numberOfGenerations):  # NEW:
            self.Spawn()  # NEW:
            self.Mutate()  # NEW:
            self.Evaluate(self.children, "DIRECT")  # NEW: Evaluate children in DIRECT mode (fast)
            self.Print()  # NEW: Print fitness of parents and children together
            self.Select()  # NEW: Compete children against parents
        # Finally, re-run the best parent's simulation in GUI mode.
        print("Done evolving ")
        self.Show_Best()  # NEW:


    def Evolve_For_One_Generation(self):
        for gen in range(c.numberOfGenerations):  # NEW:
            self.Spawn()  # NEW:
            self.Mutate()  # NEW:
            self.Evaluate(self.children, "DIRECT")  # NEW: Evaluate children in DIRECT mode (fast)
            self.Print()  # NEW: Print fitness of parents and children together
            self.Select()  # NEW: Compete children against parents

    def Evaluate(self, solutions, mode):
        for key in solutions:
            solutions[key].Start_Simulation(mode)
        for key in solutions:
            solutions[key].Wait_for_Simulation_to_End()

    def Spawn(self):
        self.children = {}  # NEW: Create an empty dictionary for children
        for key in self.parents:  # NEW:
            # Create a deep copy of each parent.
            child = copy.deepcopy(self.parents[key])
            # Assign a new unique ID to this child.
            child.Set_ID(self.nextAvailableID)  # NEW:
            self.children[key] = child  # NEW: Use the same key for correspondence.
            self.nextAvailableID += 1  # NEW:
    def Mutate(self):
        for key in self.children:
            self.children[key].Mutate()  # NEW:

    def Select(self):
        for key in self.children:
            if self.children[key].fitness < self.parents[key].fitness:
                self.parents[key] = self.children[key]  # NEW:



    def Print(self):
        print("")  # NEW: Print an empty line at the start
        for key in self.parents:
            parentFitness = self.parents[key].fitness
            # For the corresponding child (if present), get its fitness.
            childFitness = self.children[key].fitness if key in self.children else None
            print("Index", key, "| Parent fitness:", parentFitness, "| Child fitness:", childFitness)  # NEW:
        print("")  # NEW: Empty line at the end
    def Show_Best(self):
        print("show best :")
        bestKey = None
        bestFitness = None
        for key in self.parents:
            fitness = self.parents[key].fitness
            if bestFitness is None or fitness < bestFitness:
                bestFitness = fitness
                bestKey = key
        print("Best solution is at index", bestKey, "with fitness", bestFitness)  # NEW:
        # Re-run the best solution with graphics.
        self.parents[bestKey].Start_Simulation("GUI")
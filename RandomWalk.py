import random
import matplotlib.pyplot as plt


class RandomWalk:
    def __init__(self, dimensions, steps):
        # The number of dimensions you can go
        self.dimensions = dimensions
        # The amount of steps you can take
        self.steps = steps
        # Makes a matrix of amount of dimensions and amount of steps
        self.coordinate = [[0 for step in range(self.steps)] for d in range(self.dimensions)]

    def walk(self):
        # Creates a random "movement" in the array of dimensions
        for step in range(self.steps - 1):
            # A loop that goes through all the dimensions.
            # If the random dimension chosen is the current dimension, then do a side.
            # If not, stay where you are.
            random_dimensions = random.randint(0, self.dimensions)
            for dimensions in range(self.dimensions):
                if dimensions == random_dimensions:
                    self.move(dimensions, step)
                else:
                    self.stay_put(dimensions, step)

    def move(self, dimension, step):
        direction = 1
        coin_flip = random.random()
        if coin_flip < 0.5:
            direction = -1
        # Takes one step forward or back and copies to the same array with another step
        self.coordinate[dimension][step + 1] = self.coordinate[dimension][step] + direction

    def stay_put(self, d, step):
        # If he didn't take step
        self.coordinate[d][step + 1] = self.coordinate[d][step]

    def display(self):
        if self.dimensions == 1:
            plt.plot([step for step in range(self.steps)], self.coordinate[0])
            plt.show()
        elif self.dimensions == 2:
            plt.plot(self.coordinate[0], self.coordinate[1])
            plt.show()
        elif self.dimensions == 3:
            plt.subplot(111, projection="3d")
            plt.plot(self.coordinate[0], self.coordinate[1], self.coordinate[2])
            plt.show()
        else:
            for i in self.coordinate:
                for j in i:
                    print(j, end=" ")
                print()





# rw = randomWalk(3, 16)
# rw.walk()
# rw.display()

rw2 = RandomWalk(6, 10)
rw2.walk()
rw2.display()

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
        # Creates a random "movement" in the alrrauy of dimensions
        for step in range(self.steps - 1):
            # Generates a random number between 0 and a number of dimensions
            random_d = random.randint(0, self.dimensions)
            for d in range(self.dimensions):
                if d == random_d:
                    self.move(d, step)
                else:
                    self.stay_put(d, step)

    def move(self, d, step):
        direction = 1
        coin_flip = random.random()
        if coin_flip < 0.5:
            direction = -1
        self.coordinate[d][step + 1] = self.coordinate[d][step] + direction

    def stay_put(self, d, step):
        self.coordinate[d][step + 1] = self.coordinate[d][step]

    def display(self):
        if self.dimensions == 1:
            plt.plot([step for step in range(self.steps)], self.coordinate[0])
            plt.show()
        elif self.dimensions == 2:
            plt.plot(self.coordinate[0], self.coordinate[1])
            plt.show()


# rw = randomWalk(1, 16)
# rw.walk()
# rw.display()

rw2 = RandomWalk(2, 30)
rw2.walk()
rw2.display()

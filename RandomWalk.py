import random
import matplotlib.pyplot as plt


class RandomWalk:
    def __init__(self, dimensions, steps):
        self.d = dimensions
        self.steps = steps
        self.cordinate_rw = [[0 for step in range(self.steps)] for d in range(self.d)]

    def walk(self):
        for step in range(self.steps-1):
            random_d = random.randint(0, self.d)
            for d in range(self.d):
                if d == random_d:
                    self.move(d, step)
                else:
                    self.stay_put(d, step)

    def move(self, d, step):
        direction = 1
        coin_flip = random.random()
        if coin_flip < 0.5:
            direction = -1
        self.cordinate_rw[d][step+1] = self.cordinate_rw[d][step] + direction

    def stay_put(self, d, step):
        self.cordinate_rw[d][step + 1] = self.cordinate_rw[d][step]

    def display(self):
        if self.d == 1:
            plt.plot([step for step in range(self.steps)], self.cordinate_rw[0])
            plt.show()
        elif self.d == 2:
            plt.plot(self.cordinate_rw[0], self.cordinate_rw[1])
            plt.show()


# rw = randomWalk(1, 16)
# rw.walk()
# rw.display()

rw2 = RandomWalk(2, 30)
rw2.walk()
rw2.display()

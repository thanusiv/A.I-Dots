import random
from math import pi, cos, sin
from copy import deepcopy

class Brain():
    def __init__(self, size = 450):
        self.size = size
        self.directions = []
        self.randomize_directions()
        self.step = 0

    def randomize_directions(self):
        for i in range(self.size):
            self.directions.append([random.randint(-2, 2), random.randint(-2, 2)])

    def get_acceleration(self):
        return self.directions[self.step]

    def can_get_acceleration(self):
        return self.step < self.size

    def clone(self):
        clone = Brain()
        clone.directions = deepcopy(self.directions)
        return clone

    def mutate(self):
        mutation_rate = 0.05
        new_directions = []

        for direction in self.directions:
            rand = random.random()
            if rand < mutation_rate:
                new_directions.append([random.randint(-2, 2), random.randint(-2, 2)])
            else:
                new_directions.append(direction)
        self.directions = new_directions

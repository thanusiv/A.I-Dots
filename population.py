from dot import Dot
import random
from copy import deepcopy

class Population():
    def __init__(self, environment_width, environment_height, goal_x, goal_y, goal_radius, game_display, population_size = 500):
        self.environment_width = environment_width
        self.environment_height = environment_height
        self.game_display = game_display

        self.goal_x = goal_x
        self.goal_y = goal_y
        self.goal_radius = goal_radius

        self.population_size = population_size
        self.population = [Dot(environment_width, environment_height, goal_x, goal_y, goal_radius, game_display) for i in range(population_size)]

        self.generation = 1
        self.min_step = 450
    
    def update(self):
        for dot in self.population:
            if dot.brain.step > self.min_step:
                dot.dead = True
            dot.update()
    
    def are_all_dots_dead(self):
        for dot in self.population:
            if not dot.dead:
                return False
        return True

    def natural_selection(self, fitness_sum):
        new_dots = []
        best_dot = self.get_best_dot()
        if (best_dot.reach_goal):
            self.min_step = best_dot.brain.step
        new_dots.append(best_dot.get_offspring())
        new_dots[0].is_best = True

        for i in range(self.population_size - 1): # since we added the best dot
            parent = self.select_parent(fitness_sum)
            new_dots.append(parent.get_offspring())
        
        self.population = new_dots
        self.generation += 1

    def calculate_fitness_sum(self):
        fitness_sum = 0
        for dot in self.population:
            fitness_sum += dot.calculate_fitness()
        return fitness_sum

    def select_parent(self, fitness_sum):
        value = random.uniform(0, fitness_sum)
        running_sum = 0
        for dot in self.population:
            running_sum += dot.calculate_fitness()
            if running_sum > value:
                return dot

    def mutate_offsprings(self):
        for dot in self.population[1:]: # do not mutate previous gen best dot
            dot.brain.mutate()

    def get_best_dot(self):
        max_fitness = 0
        best_dot = None

        for dot in self.population:
            fitness = dot.calculate_fitness()
            if fitness > max_fitness:
                best_dot = dot
                max_fitness = fitness

        return best_dot

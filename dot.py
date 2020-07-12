import pygame
from brain import Brain
from math import sqrt

class Dot():
    def __init__(self, environment_width, environment_height, goal_x, goal_y, goal_radius, game_display):
        self.environment_width = environment_width
        self.environment_height = environment_height

        self.goal_x = goal_x
        self.goal_y = goal_y
        self.goal_radius = goal_radius

        self.position = [environment_width // 2, environment_height - 20]
        self.velocity = [0, 0]
        self.acceleration = [0, 0]
        self.radius = 2
        
        self.game_display = game_display
        self.black = (0,0,0)
        self.green = (0,255,0)
        
        self.dead = False
        self.reach_goal = False
        self.is_best = False

        self.brain = Brain()
    
    def show(self):
        if (self.is_best):
            pygame.draw.circle(self.game_display, self.green, self.position, 5)
        else:
            pygame.draw.circle(self.game_display, self.black, self.position, self.radius)
    
    def move(self):
        if self.brain.can_get_acceleration():
            self.acceleration = self.brain.get_acceleration()
            self.brain.step += 1
        else:
            self.dead = True
            return
        
        self.velocity[0] += self.acceleration[0]
        self.velocity[1] += self.acceleration[1]

        self.limit_velocity_check() # can comment out if wanted
        
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

    def limit_velocity_check(self):
        if self.velocity[0] < -4:
            self.velocity[0] = -4
        if self.velocity[1] < -4:
            self.velocity[1] = -4
        if self.velocity[0] > 4:
            self.velocity[0] = 4
        if self.velocity[1] > 4:
            self.velocity[1] = 4

    def collision_check(self):
        collision_with_goal = self.get_distance_to_goal() < float(self.goal_radius + self.radius)
        #collision_with_obstacle 

        if self.position[0] - 4 <= 0 or self.position[0] + 4 >= self.environment_width or \
            self.position[1] - 4 <= 0 or self.position[1] + 4 >= self.environment_height:
            self.dead = True
        elif collision_with_goal:
            self.reach_goal = True
            self.dead = True
    
    def get_distance_to_goal(self):
        return sqrt((self.position[0] - self.goal_x) ** 2 + (self.position[1] - self.goal_y) ** 2)

    #def collision_with_obstacle(self):
    #    if self.position[0] - 4 >= 
    
    def update(self):
        if not self.dead:
            self.move()
            self.collision_check()
        self.show()

    def calculate_fitness(self):
        if (self.reach_goal):
            fitness = 1.0/16.0 + 10000.0/(self.brain.step * self.brain.step)
        else:
            distance_to_goal = self.get_distance_to_goal()
            fitness = 1.0/(distance_to_goal * distance_to_goal)
        return fitness

    def get_offspring(self): # crossover with single parent
        offspring = Dot(self.environment_width, self.environment_height, self.goal_x, self.goal_y, self.goal_radius, self.game_display)
        offspring.brain = self.brain.clone()
        return offspring
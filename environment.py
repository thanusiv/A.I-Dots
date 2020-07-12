import pygame
from population import Population
from goal import Goal
from obstacle import Obstacle

class Environment():

    def __init__(self, environment_width, environment_height):
        self.white = (255,255,255)
        self.environment_width = environment_width
        self.environment_height = environment_height

        pygame.init()
        self.game_display = pygame.display.set_mode((environment_width, environment_height))
        self.clear_screen()

        self.goal_x = environment_width // 2
        self.goal_y = 30
        self.goal_radius = 5
        self.goal = Goal(self.goal_x, self.goal_y, self.goal_radius, self.game_display)

        self.population = Population(environment_width, environment_height, self.goal_x, self.goal_y, self.goal_radius, self.game_display)
        # self.obstacle = Obstacle(environment_width, environment_height, self.game_display, 200, 200, 500, 10)
       
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if self.population.are_all_dots_dead():
            fitness_sum = self.population.calculate_fitness_sum()
            self.population.natural_selection(fitness_sum)
            self.population.mutate_offsprings()
        else:
            self.clear_screen()
            # self.obstacle.show()
            self.goal.show()
            self.population.update()
            pygame.time.wait(20)
            pygame.display.update()

    def clear_screen(self):
        self.game_display.fill(self.white)

import pygame


class Obstacle():
    def __init__(self, environment_width, environment_height, game_display):
        self.environment_width = environment_width
        self.environment_height = environment_height
        self.game_display = game_display
        
        self.red = (255, 0, 0)

    def show(self):
        pygame.draw.circle(self.game_display, self.red, [self.environment_width // 2, self.environment_height // 2], 60)

    def collision_check(self):
        pass
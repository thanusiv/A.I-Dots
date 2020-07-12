import pygame


class Obstacle():
    def __init__(self, environment_width, environment_height, game_display, top_left_x, top_left_y, length, width):
        self.environment_width = environment_width
        self.environment_height = environment_height
        self.game_display = game_display
        
        self.red = (255, 0, 0)
        self.top_left_x = top_left_x
        self.top_left_y = top_left_y
        self.length = length
        self.width = width
        self.rect = pygame.Rect(top_left_x, top_left_y, length, width)

    def show(self):
        pygame.draw.rect(self.game_display, self.red, self.rect)

    def collision_check(self):
        pass
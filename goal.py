import pygame

class Goal():
    def __init__(self, x, y, radius, game_display):
        self.position = [x, y]
        self.radius = radius
        
        self.game_display = game_display
        self.blue = (0,0,255)
    
    def show(self):
        pygame.draw.circle(self.game_display, self.blue, self.position, self.radius)
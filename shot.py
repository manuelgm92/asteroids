import pygame
import constants
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, radius=constants.SHOT_RADIUS)
        
        
    def draw(self, screen, color="White", width=None):
        width = constants.LINE_WIDTH
        pygame.draw.circle(screen, color, self.position, self.radius, width)
             
    def update(self, dt):
        self.position += self.velocity * dt   
import circleshape
import constants
import pygame

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen, color="White", width=None):
        width = constants.LINE_WIDTH
        pygame.draw.circle(screen, color, self.position, self.radius, width)
         
    def update(self, dt):
        self.position += self.velocity * dt
        
    

import circleshape
import constants
import pygame
import random
from logger import log_event

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen, color="White", width=None):
        width = constants.LINE_WIDTH
        pygame.draw.circle(screen, color, self.position, self.radius, width)
         
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            pygame.sprite.Sprite.kill(self)
        else:
            pygame.sprite.Sprite.kill(self)

            log_event("asteroid_split")
            new_angle = random.uniform(20, 50)
            
            position_asteroid_1 = pygame.math.Vector2.rotate(self.velocity, new_angle)
            position_asteroid_2  = pygame.math.Vector2.rotate(self.velocity, -new_angle)
            new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
            
            new_asteroid_1 = Asteroid(self.position.x, self.position.y, radius=new_radius)
            new_asteroid_2 = Asteroid(self.position.x, self.position.y, radius=new_radius)
            
            new_asteroid_1.velocity = position_asteroid_1 * 1.2
            new_asteroid_2.velocity = position_asteroid_2 * 1.2
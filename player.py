from circleshape import CircleShape
import constants
import pygame

class Player(CircleShape):
    def __init__(self, x, y, radius=constants.PLAYER_RADIUS):
        super().__init__(x, y, radius)
        self.rotation = 0
        
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen, color="White", points=None, width=constants.LINE_WIDTH):
        if points == None:
            points = self.triangle()
        return pygame.draw.polygon(screen, color, points, width)

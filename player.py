from circleshape import CircleShape
import constants
import pygame
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y, radius=constants.PLAYER_RADIUS):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.shot_cooldown = 0
        
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

    def rotate(self, dt):
        self.rotation += constants.PLAYER_TURN_SPEED * dt
        return self.rotation
    
    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)    
        if keys[pygame.K_SPACE]:
            if self.shot_cooldown > 0:
                pass  
            else:
                self.shoot()
                self.shot_cooldown = constants.PLAYER_SHOOT_COOLDOWN_SECONDS 
            
        self.shot_cooldown -= dt
 
    def move(self, dt):
        unit_vector = pygame.Vector2(0,1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * constants.PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector
        
    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        shot_vector = pygame.Vector2(0,1)
        rotated_shot_vector = shot_vector.rotate(self.rotation)
        rotated_shot_with_speed_vector = rotated_shot_vector * constants.PLAYER_SHOOT_SPEED
        shot.velocity = rotated_shot_with_speed_vector
        
        
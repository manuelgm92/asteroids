import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print("Screen width: 1280\nScreen height: 720")
    pygame.init()

if __name__ == "__main__":
    main()
    
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

while True:
    log_state()
    
    for event in pygame.event.get():
        pass
    
    screen.fill("black")

    pygame.display.flip()

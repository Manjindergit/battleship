import pygame
from logger import log_state
from constants import *

def main():
    print("Hello from battleship!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    running = True
    
    while running:
        
        log_state()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        screen.fill("yellow")
        
        pygame.display.flip()
        clock.tick(60)  # limits FPS to 60

if __name__ == "__main__":
    main()
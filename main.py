import pygame
from logger import log_state
from constants import *
import player


def main():
    print("Hello from battleship!")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    running = True
    dt = 0
    p1 = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    
    while running:
        
        log_state()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        screen.fill("yellow")
        p1.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60)/1000 # delay game to 1/60 of second to prevent resource consumption and control frame rate
        

if __name__ == "__main__":
    main()
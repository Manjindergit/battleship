import pygame
from logger import log_state
from constants import *
from player import Player


def main():
    print("Hello from battleship!")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    running = True
    dt = 0
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
   
    
    while running:
        
        log_state()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        updateable.update(dt)
        screen.fill("yellow")
        for obj in drawable:
            obj.draw(screen)
        
        
        
        pygame.display.flip()
        dt = clock.tick(60)/1000 # delay game to 1/60 of second to prevent resource consumption and control frame rate
        

if __name__ == "__main__":
    main()
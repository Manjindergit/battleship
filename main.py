import sys
import pygame
from logger import log_state, log_event
from constants import *
from player import Player
from asteroid import Asteroid
from sprite.asteroidfield import AsteroidField


def main():
    print("Hello from battleship!")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    running = True
    dt = 0
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroid_field = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable,)
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
       
    while running:
        
        log_state()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        updateable.update(dt)
        for obj in asteroids:
            if obj.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
                
        screen.fill("yellow")
        for obj in drawable:
            obj.draw(screen) 
        
        pygame.display.flip()
        dt = clock.tick(60)/1000 # delay game to 1/60 of second to prevent resource consumption and control frame rate

if __name__ == "__main__":
    main()
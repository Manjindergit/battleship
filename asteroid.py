import pygame
import random
from sprite.circleshape import CircleShape
from constants import *
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, LINE_WIDTH)
        
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20, 50)
            asteroid_child1_angle = self.velocity.rotate(random_angle)
            asteroid_child2_angle = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_child1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_child2 = Asteroid(self.position.x, self.position.y, new_radius)
            
            asteroid_child1.velocity = asteroid_child1_angle * 1.2
            asteroid_child2.velocity = asteroid_child2_angle * 1.2
            
            
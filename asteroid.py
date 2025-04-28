# A class for the asteroid objects
import random
from circleshape import *
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, white, (self.position), self.radius, width=2) # Draws the asteroid to the screen

    def update(self, dt):
        self.position += self.velocity * dt # Increases the speed by the delta time
    
    # Function to split asteroids hit with shot
    def split(self):
        # Kills small asteroids
        if self.radius <= ASTEROID_MIN_RADIUS:
            return self.kill()
        # Splits med/large asteroids
        else:
            random_angle = random.uniform(20, 50)
            new_velocity1 = self.velocity.rotate(random_angle) # Random angles for each to travel away from the original path (between 20 - 50 degrees)
            new_velocity2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS # Shrinks the split asteroids into the next smallest size
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius) # Makes two new asteroid objects at the location of the old
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = new_velocity1 * 1.2 # Sets the speed of the split asteroids to the random angles * 120%
            asteroid2.velocity = new_velocity2 * 1.2
            self.kill() # Kills the original asteroid
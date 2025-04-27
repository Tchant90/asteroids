# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import AsteroidField

def main():
    pygame.init() # Initializes pygame
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Creates the game screen set to the predetermined width and height
    pygame.display.set_caption("Asteroids") # Sets the title of the window

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable, )

    clock = pygame.time.Clock() # Clock object used to set the refresh rate w/ dt
    player = Player() # Player object
    asteroid_field = AsteroidField()
    
    # Infinite while loop that keeps the window open and the game running, quits if user closes window or ctrl + c from the cli
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(black) # Fills the screen with the color black
        for sprite in drawable: # Loops over all objects in the drawable group, draws them to the screen
            sprite.draw(screen)
        pygame.display.flip() # Refreshes the screen
        dt = clock.tick(60) / 1000 # Calculates the refresh rate in milliseconds
        updatable.update(dt) # Updates the delta time (dt) variable for use in the updateable group functions
        for asteroid in asteroids:
            if asteroid.collisioncheck(player):
                print("Game over!")
                import sys
                sys.exit()

    pygame.quit() # Quits the game

if __name__ == "__main__": # Another infinite loop set to true that runs the main() function
    main() # Run the main() function
# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from circleshape import *
from player import *

def main():
    pygame.init() # Initializes pygame
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Creates the game screen set to the predetermined width and height
    pygame.display.set_caption("Asteroids") # Sets the title of the window

    clock = pygame.time.Clock() # Clock object used to set the refresh rate w/ dt
    player = Player() # Player object


    updatable = pygame.sprite.Group(player)
    drawable = pygame.sprite.Group(player)
    Player.containers = (updatable, drawable)

    # Infinite while loop that keeps the window open and the game running, quits if user closes window or ctrl + c from the cli
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(black) # Fills the screen with the color black
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip() # Refreshes the screen
        dt = clock.tick(60) / 1000 # Calculates the refresh rate in milliseconds
        updatable.update(dt) # Updates the delta time (dt) variable for use in the player update() and rotate() functions

    pygame.quit() # Quits the game

if __name__ == "__main__": # Another infinite loop set to true that runs the main() function
    main() # Run the main() function
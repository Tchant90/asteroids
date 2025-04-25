from circleshape import *
from constants import *

# Child class of CircleShape
class Player(CircleShape):
    def __init__(self):
        super().__init__(x, y, PLAYERS_RADIUS)
        self.rotation = 0
    
    # Sets the player's sprite as a triangle instead of a circle
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    # Sets the players triangle shape, line width, and color
    def draw(self, screen):
        pygame.draw.polygon(screen, white, self.triangle(), width=2)
    
    # A function for how quickly to rotate the character model
    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

    # Updates the model's rotation based on which keys get pressed - a for left, d for right rotation.  Rotation speed is based on dt
    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

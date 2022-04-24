import pygame  # Library with functions to create the game itself.
import os  # Library that allows you to integrate the code with the game's icons in the folder.
import random

from soupsieve import (
    select,
)  # The random, is to create the random position of the obstacles.

# 01. The constant values of the game:

# The screen configurations.
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800

# Take the images in the "icons" folder, and enlarge them by 2x,
# so they don't get too small on the screen.
BACKGROUND_ICON = pygame.transform.scale2x(
    pygame.image.load(os.path.join("icons", "bg.png"))
)
BASE_ICON = pygame.transform.scale2x(
    pygame.image.load(os.path.join("icons", "base.png"))
)
PIPE_ICON = pygame.transform.scale2x(
    pygame.image.load(os.path.join("icons", "pipe.png"))
)
# "Icons", because we have three different frames of the bird.
# And since the method must be repeated three times, it goes in a list.
BIRD_ICONS = [
    pygame.transform.scale2x(pygame.image.load(os.path.join("icons", "bird1.png"))),
    pygame.transform.scale2x(pygame.image.load(os.path.join("icons", "bird2.png"))),
    pygame.transform.scale2x(pygame.image.load(os.path.join("icons", "bird3.png"))),
]

# Configure game text and messages.
pygame.font.init()
SCORE_FONT = pygame.font.SysFont("arial", 50)


# 2. Game objects:


class Bird:  # Object Bird

    # Bird Constant Values.
    B_ICONS = BIRD_ICONS
    # Bird rotation animations.
    MAXIMUM_ROTATION = 25
    ROTATION_SPEED = 20
    ANIMATION_TIME = 5

    # class Bird Attributes.
    def __init__(self, x, y):
        self.x = x  # x for x axis position.
        self.y = y  # y for y axis position.
        self.angle = 0  # Inclination of the bird at the beginning of the game.
        self.velocity = 0  # Bird speed at the beginning of the game.
        self.height = self.y  # Bird position at the beginning of the game.
        # Auxiliary parameters.
        self.time = 0  # The time of the bird's animation cycle.
        self.count_icon = 0  # Define the cycle of the bird's frames (icons).
        self.icon = BIRD_ICONS[0]  # Which icon does the bird start.

    def jump(self):
        """Function responsible for making the bird jump, resetting
        the animation time and adding speed (as in pygame the y axis
        is inverted, we subtract from the speed for the bird to go up)."""
        self.velocity = -10.5
        self.time = 0
        self.height = self.y

    def move(self):
        """Function responsible for making the bird animation cicle."""
        # Calculate the move.
        self.time += 1
        displacement = 1.5 * (self.time**2) + self.velocity * self.time

        # Restrict movement.
        if displacement > 16:
            displacement = 16

        elif displacement < 0:
            displacement -= 2

        self.y += displacement

        # Calculate the cycle of the bird's animations.
        if displacement < 0 or self.y < (self.height + 50):
            if self.angle < self.MAXIMUM_ROTATION:
                self.angle = self.MAXIMUM_ROTATION

        else:
            if self.angle > -90:
                self.angle -= self.ROTATION_SPEED

    def draw():
        # choose an icon.

        # change icon.

        # Draw icon.
        pass


class Pipe:  # Object Pipe
    # Pipe Constant Values.
    pass


class Ground:  # Object Ground
    # Ground Constant Values.
    pass

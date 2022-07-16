# Import the pygame module
import pygame

from SnopClass import Snop

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

from SnopClass import Snop

# Initialize pygame
pygame.init()

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_DIMS = (SCREEN_WIDTH, SCREEN_HEIGHT)

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode(SCREEN_DIMS)
surf = pygame.Surface(SCREEN_DIMS)
# Variable to keep the main loop running
running = True

# Main loop
bg = pygame.image.load("bg.png")

# INSIDE OF THE GAME LOOP

snop = Snop((100, 100), pygame.Color(255, 0, 0), 6, SCREEN_DIMS)
while running:
    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False

        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False
        if pygame.mouse.get_pressed()[0]:
            testsnop = Snop(pygame.mouse.get_pos(),
                            pygame.Color(255, 0, 0), 6, SCREEN_DIMS)
            testsnop.find(screen)
            snop = Snop(testsnop.maxCircle[1], pygame.Color(
                255, 0, 0), 6, SCREEN_DIMS)
            snop.find(screen)

    snop.draw(screen)
    pygame.display.update()

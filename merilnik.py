# Import the pygame module
import pygame

from Snop import Snop
from SliderClass import Slider


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
clock = pygame.time.Clock()
# INSIDE OF THE GAME LOOP

snop = Snop((100, 100), pygame.Color(255, 0, 0), 6, SCREEN_DIMS)
testsnop = Snop((100, 100), pygame.Color(255, 0, 0), 6, SCREEN_DIMS)

lines = 6
input_rect = pygame.Rect(250, 20, 140, 32)
base_font = pygame.font.Font(None, 32)
user_text = ''
color = pygame.Color(100, 100, 100)


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
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            else:
                user_text += event.unicode

        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False

        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            if pos[1] > 100:
                testsnop = Snop(pos,pygame.Color(255, 0, 0), lines, SCREEN_DIMS)
                if(testsnop.find(screen) == False):
                    snop.reset()
                    continue

            snop = Snop(testsnop.circle[1].get(),pygame.Color(255, 0, 0), lines, SCREEN_DIMS)
            snop.find(screen)
            try:
                dpi = int(user_text)
                size = snop.circle[0]/dpi*254
                print(size)
            except:
                continue
    snop.draw(screen)
    #testsnop.draw(screen)
    pygame.draw.rect(screen, color, input_rect)

    text_surface = base_font.render(user_text, True, (255, 255, 255))

    # render at position stated in arguments
    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))

    # set width of textfield so that text cannot get
    # outside of user's text input
    input_rect.w = max(100, text_surface.get_width()+10)

    # display.flip() will update only a portion of the
    # screen to updated, not full area
    pygame.display.flip()

    # snop.draw(screen)
    clock.tick(30)
    pygame.display.update()

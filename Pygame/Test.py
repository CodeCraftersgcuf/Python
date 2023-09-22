import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((400, 300))

# Set the background color to blue
background_color = (0, 0, 255)

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with the background color
    screen.fill(background_color)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()

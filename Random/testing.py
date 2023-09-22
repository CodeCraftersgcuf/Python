import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SPEED = 5
OBJECT_SPEED = 3

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Collect Objects Game")

# Define the player
player = pygame.image.load("player.png")
player_rect = player.get_rect()
player_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# Create objects and obstacles
objects = []
obstacles = []
for _ in range(10):
    object = pygame.image.load("object.png")
    object_rect = object.get_rect()
    object_rect.topleft = (random.randint(0, SCREEN_WIDTH - object_rect.width), random.randint(0, SCREEN_HEIGHT - object_rect.height))
    objects.append(object_rect)

for _ in range(5):
    obstacle = pygame.image.load("obstacle.png")
    obstacle_rect = obstacle.get_rect()
    obstacle_rect.topleft = (random.randint(0, SCREEN_WIDTH - obstacle_rect.width), random.randint(0, SCREEN_HEIGHT - obstacle_rect.height))
    obstacles.append(obstacle_rect)

# Game loop
running = True
score = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        player_rect.x += PLAYER_SPEED
    if keys[pygame.K_UP]:
        player_rect.y -= PLAYER_SPEED
    if keys[pygame.K_DOWN]:
        player_rect.y += PLAYER_SPEED

    # Check for collisions between player and objects
    for object_rect in objects[:]:
        if player_rect.colliderect(object_rect):
            objects.remove(object_rect)
            score += 10

    # Check for collisions between player and obstacles
    for obstacle_rect in obstacles:
        if player_rect.colliderect(obstacle_rect):
            running = False

    # Move objects and obstacles
    for object_rect in objects:
        object_rect.x += OBJECT_SPEED
        if object_rect.right > SCREEN_WIDTH:
            object_rect.left = 0

    for obstacle_rect in obstacles:
        obstacle_rect.x -= OBJECT_SPEED
        if obstacle_rect.left < 0:
            obstacle_rect.right = SCREEN_WIDTH

    # Draw everything
    screen.fill(WHITE)
    for object_rect in objects:
        screen.blit(object, object_rect)
    for obstacle_rect in obstacles:
        screen.blit(obstacle, obstacle_rect)
    screen.blit(player, player_rect)

    # Display score
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, RED)
    screen.blit(text, (10, 10))

    pygame.display.flip()

# Quit Pygame
pygame.quit()

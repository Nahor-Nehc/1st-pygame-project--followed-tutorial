import pygame
import os
WIDTH, HEIGHT = 900, 500

# ship
VEL = 4
SPACESHIP_SIZE = (76, 68)
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, SPACESHIP_SIZE), 90)
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_red.png"))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_SIZE)), 270)

# bullets
BULLET_VEL = 7
MAX_BULLETS = 6
BULLET_WIDTH, BULLET_HEIGHT = 30, 280

# ammo
YELLOW_AMMO_BAR = pygame.Rect(10, HEIGHT - BULLET_HEIGHT - 10, BULLET_WIDTH, BULLET_HEIGHT)
RED_AMMO_BAR = pygame.Rect(WIDTH - BULLET_WIDTH - 10, HEIGHT - BULLET_HEIGHT - 10, BULLET_WIDTH, BULLET_HEIGHT)

# other
SPACE = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "space.png")), (WIDTH, HEIGHT))
import pygame
import os
import math
import random
import socket
from network import Network
from Components.format_data import convert
from Components.settings import *

pygame.font.init()
pygame.mixer.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spaceships")

BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

SPECIAL_WIDTH = 70

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
dimRED = (200, 0, 0)
dimGREEN = (0, 200, 0)
dimBLUE = (0, 0, 200)

YELLOW_AMMO_BAR = pygame.Rect(10, HEIGHT - BULLET_HEIGHT - 10, BULLET_WIDTH, BULLET_HEIGHT)
RED_AMMO_BAR = pygame.Rect(WIDTH - BULLET_WIDTH - 10, HEIGHT - BULLET_HEIGHT - 10, BULLET_WIDTH, BULLET_HEIGHT)

BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join("Assets", "Gunsound2.mp3"))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join("Assets", "Grenade+1.mp3"))

FONT = pygame.font.SysFont("calibri", 40)
WINNER_FONT = pygame.font.SysFont("calibri", 100)

FPS = 60

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

class Spaceship:
  def __init__(self, x, y, width, height, image):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.update()
    self.image = image
  
  def move(self, keys_pressed):
    if keys_pressed[pygame.K_a] and self.x - VEL > 0: #left
      self.x -= VEL
    if keys_pressed[pygame.K_d] and self.x + self.width + VEL < BORDER.x: # right
      self.x += VEL
    if keys_pressed[pygame.K_w] and self.y - VEL > 0: # up
      self.y -= VEL
    if keys_pressed[pygame.K_s] and self.y + VEL + self.height < HEIGHT - 10: # down
      self.y += VEL
    
    self.update()
  
  def draw(self, window):
    pass
  
  def update(self):
    self.rect = (self.x, self.y, self.width, self.height)

def draw():

  pygame.display.update()

def make_data(string):
  pass

def unmake_data(string):
  pass

def main():

  state = "menu"
  network = Network()
  data = convert(network.get_init_pos())
  
  p1 = Spaceship(data[0], data[1], data[2], data[3])

  clock = pygame.time.Clock()
  run = True
  while run:
    clock.tick(FPS)
    for event in pygame.event.get():
      mouse = pygame.mouse.get_pos()
      if event.type == pygame.QUIT:#quit event
        run = False
        pygame.quit()

      if event.type == pygame.KEYDOWN:
        pass
      
    if state == "game":
      keys_pressed = pygame.key.get_pressed()
      p1.move(keys_pressed, VEL)

    draw()

  main()


if __name__ == "__main__":
  main()
import pygame
import os
import math
import random
import socket
import sys
from network import Network
from Components.format_data import convert_initial_message, build_client_reply, unpack_server_reply
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

BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join("Assets", "Gunsound2.mp3"))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join("Assets", "Grenade+1.mp3"))

FONT = pygame.font.SysFont("calibri", 40)
WINNER_FONT = pygame.font.SysFont("calibri", 100)

FPS = 60

class Spaceship:
  def __init__(self, x, y, width, height, image, current_player):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.update()
    self.image = image
    self.bullet_to_fire = tuple()
    self.number = current_player
  
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
    window.blit(self.image, (self.x, self.y))
  
  def update(self):
    self.rect = (self.x, self.y, self.width, self.height)
  
  def shoot(self):
    bullet_position = tuple()#
    self.bullet_to_fire = bullet_position
  
  def take_bullet(self):
    temp = self.bullet_to_fire
    self.bullet_to_fire = tuple()
    return temp

  def set(self, x, y, width, height):
    self.x = x
    self.y = y
    self.width = width
    self.height = height

def draw(WIN, player, enemy):
  WIN.blit(SPACE, (0, 0))
  player.draw(WIN)
  enemy.draw(WIN)

  pygame.display.update()

def main():

  state = "game"
  network = Network()
  data = convert_initial_message(network.get_init_pos())
  print(data)
  
  player_number = data[4]
  enemy_number = int(not player_number)
  if player_number == 0:
    spaceship_image = YELLOW_SPACESHIP
    enemy_spaceship_image = RED_SPACESHIP
  elif player_number == 1:
    spaceship_image = RED_SPACESHIP
    enemy_spaceship_image = YELLOW_SPACESHIP
  else:
    raise ValueError("player number not 0 or 1:", player_number)
  player = Spaceship(data[0], data[1], data[2], data[3], spaceship_image, player_number)
  enemy = Spaceship(data[5], data[6], data[7], data[8], enemy_spaceship_image, enemy_number)

  clock = pygame.time.Clock()
  run = True
  while run:
    clock.tick(FPS)
    enemy_ship, bullet_enemy, bullet_player, enemy_ammo, enemy_sb_charge = unpack_server_reply(network.send(build_client_reply(player.rect, player.take_bullet())))
    for event in pygame.event.get():
      mouse = pygame.mouse.get_pos()
      if event.type == pygame.QUIT:#quit event
        run = False
        pygame.quit()
        sys.exit()
      if state == "game":
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
            player.shoot()
      
    if state == "game":
      keys_pressed = pygame.key.get_pressed()
      player.move(keys_pressed)
      print(enemy_ship)
      enemy.set(*map(int, enemy_ship))

    draw(WIN, player, enemy)

  main()

if __name__ == "__main__":
  main()
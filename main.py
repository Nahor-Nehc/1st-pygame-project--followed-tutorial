import pygame
import os
import math
import random


pygame.font.init()
pygame.mixer.init()

global VEL, BULLET_VEL, SPECIAL_WIDTH, MAX_BULLETS, settings, settingsChange, settingsDefault, settingsNAme, settingsMax, settingsMin

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spaceships")

AMMO_WIDTH, AMMO_HEIGHT = 30, 280

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

BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

YELLOW_AMMO_BAR = pygame.Rect(10, HEIGHT - AMMO_HEIGHT - 10, AMMO_WIDTH, AMMO_HEIGHT)
RED_AMMO_BAR = pygame.Rect(WIDTH - AMMO_WIDTH - 10, HEIGHT - AMMO_HEIGHT - 10, AMMO_WIDTH, AMMO_HEIGHT)

BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join("Assets", "Gunsound2.mp3"))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join("Assets", "Grenade+1.mp3"))

FONT = pygame.font.SysFont("calibri", 40)
WINNER_FONT = pygame.font.SysFont("calibri", 100)

FPS = 60
VEL = 4
BULLET_VEL = 7
MAX_BULLETS = 6
SPACESHIP_SIZE = (76, 68)


YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2


YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, SPACESHIP_SIZE), 90)
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_red.png"))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_SIZE)), 270)
SPACE = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "space.png")), (WIDTH, HEIGHT))


MAX_AMMO = 7.1
RELOAD_SPEED = 1

MAX_CHARGE = 7.1

BUTTONWIDTH, BUTTONHEIGHT = 500, 50
bw, bh = BUTTONWIDTH, BUTTONHEIGHT

PLAYBUTTONx, PLAYBUTTONy = WIDTH/2 - bw/2, 400
pbx, pby = PLAYBUTTONx, PLAYBUTTONy

CHANGEBUTTONWIDTH, CHANGEBUTTONHEIGHT = 50, 50
cbw, cbh = CHANGEBUTTONWIDTH, CHANGEBUTTONHEIGHT

baddx = pbx + bw - cbw
bminusx = pbx

settings = [VEL, BULLET_VEL, SPECIAL_WIDTH, MAX_BULLETS]
settingsMin = [1, 1, 5, 1]
settingsMax = [20, 20, 200, 10]
settingsNAme = ["Spaceship speed", "Bullet speed", "SB width", "Max bullets"]
settingsDefault = [4, 7, 70, 6]
settingsChange = [1, 1, 5, 1]

def drawWindow(red, yellow, redBullets, yellowBullets, redHealth, yellowHealth, redAmmo, yellowAmmo, redCharge, yellowCharge, screenState, mouse, settingsName, settings, VEL):

  if screenState == "menu":

    WIN.blit(SPACE, (0, 0))

    playText = FONT.render("Play", 1, BLACK)
    
    if pbx <= mouse[0] <= pbx + bw and pby <= mouse[1] <= pby + bh:
      pygame.draw.rect(WIN, dimGREEN, pygame.Rect(pbx, pby, bw, bh))
    else:
      pygame.draw.rect(WIN, GREEN, pygame.Rect(pbx, pby, bw, bh))
    
    WIN.blit(playText, (pbx + bw/2 - playText.get_width()/2, pby + bh/2 - playText.get_height()/2))

    addText = FONT.render("+", 1, BLACK)
    minusText = FONT.render("-", 1, BLACK)

    for button in range (1, 5):
      height = (70 * button) - 40

      if baddx <= mouse[0] <= baddx + cbw and height <= mouse[1] <= height + cbh:
        pygame.draw.rect(WIN, dimGREEN, pygame.Rect(baddx, height, cbw, cbh))
      else:
        pygame.draw.rect(WIN, GREEN, pygame.Rect(baddx, height, cbw, cbh))
      
      WIN.blit(addText, (baddx + cbw/2 - addText.get_width()/2, height + cbh/2 - addText.get_height()/2))

    for button in range (1, 5):
      height = (70 * button) - 40

      if bminusx <= mouse[0] <= bminusx + cbw and height <= mouse[1] <= height + cbh:
        pygame.draw.rect(WIN, dimGREEN, pygame.Rect(bminusx, height, cbw, cbh))
      else:
        pygame.draw.rect(WIN, GREEN, pygame.Rect(bminusx, height, cbw, cbh))
      
      WIN.blit(minusText, (bminusx + cbw/2 - minusText.get_width()/2, height + cbh/2 - minusText.get_height()/2))

    for label in range (1, 5):
      height = (70 * label) - 40
      Text = FONT.render(settingsName[label - 1] + ": " + str(settings[label - 1]), 1, BLACK)

      pygame.draw.rect(WIN, GREEN, pygame.Rect(bminusx + cbw + 10, height, bw - 20 - (cbw*2), bh))

      WIN.blit(Text, (bminusx + cbw + 20, height + cbh - Text.get_height()))

    resetText = FONT.render("Reset", 1, BLACK)
    
    if pbx <= mouse[0] <= pbx + bw and pby - bh - 10 <= mouse[1] <= pby - 10:
      pygame.draw.rect(WIN, dimGREEN, pygame.Rect(pbx, pby - bh - 10, bw, bh))
    else:
      pygame.draw.rect(WIN, GREEN, pygame.Rect(pbx, pby - bh - 10, bw, bh))
    
    WIN.blit(resetText, (pbx + bw/2 - playText.get_width()/2, pby + bh/2 - playText.get_height()/2 - bh - 10))





  elif screenState == "game":
    WIN.blit(SPACE, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))

    #-----------------------------------------------------
    pygame.draw.rect(WIN, GREEN, YELLOW_AMMO_BAR)
    pygame.draw.rect(WIN, GREEN, RED_AMMO_BAR)

    maxSize = MAX_AMMO * 40
    yellowSize = yellowAmmo * 40
    redSize = redAmmo * 40

    pygame.draw.rect(WIN, RED, pygame.Rect(10, HEIGHT - AMMO_HEIGHT - 10, AMMO_WIDTH, maxSize - yellowSize - 5))
    pygame.draw.rect(WIN, RED, pygame.Rect(WIDTH - AMMO_WIDTH - 10, HEIGHT - AMMO_HEIGHT - 10, AMMO_WIDTH, maxSize - redSize - 5))
    
    for line in range(1, 7):
      pygame.draw.rect(WIN, BLACK, pygame.Rect(10, HEIGHT - AMMO_HEIGHT + (line*40) - 12, AMMO_WIDTH, 2))
      pygame.draw.rect(WIN, BLACK, pygame.Rect(WIDTH - AMMO_WIDTH - 10, HEIGHT - AMMO_HEIGHT + (line*40) - 12, AMMO_WIDTH, 2))

    #-----------------------------------------------------

    pygame.draw.rect(WIN, YELLOW, pygame.Rect(50, HEIGHT - AMMO_HEIGHT - 10 + maxSize - (yellowCharge*40), 5, yellowCharge*40 - 4))

    pygame.draw.rect(WIN, YELLOW, pygame.Rect(WIDTH - 55, HEIGHT - AMMO_HEIGHT - 10 + maxSize - (redCharge*40), 5, redCharge*40 - 4))

    if yellowCharge >= 7:
      pygame.draw.circle(WIN, YELLOW, (52.5, HEIGHT - AMMO_HEIGHT - 25), 6)

    if redCharge >= 7:
      pygame.draw.circle(WIN, YELLOW, (WIDTH - 52.5, HEIGHT - AMMO_HEIGHT - 25), 6)
    #-----------------------------------------------------

    redHealth_text = FONT.render("Health: " + str(redHealth), 1, WHITE)
    yellowHealth_text = FONT.render("Health: " + str(yellowHealth), 1, WHITE)

    WIN.blit(redHealth_text, (WIDTH - redHealth_text.get_width() - 10, 10))
    WIN.blit(yellowHealth_text, (10, 10))

    redAmmo_text = FONT.render(str(math.floor(redAmmo)), 1, WHITE)
    yellowAmmo_text = FONT.render(str(math.floor(yellowAmmo)), 1, WHITE)

    WIN.blit(redAmmo_text, (WIDTH - AMMO_WIDTH - 10, HEIGHT - AMMO_HEIGHT - 60))
    WIN.blit(yellowAmmo_text, (10, HEIGHT - AMMO_HEIGHT - 60))

    for bullet in redBullets:
      pygame.draw.rect(WIN, RED, bullet)

    for bullet in yellowBullets:
      pygame.draw.rect(WIN, YELLOW, bullet)

  pygame.display.update()

def yellowMove(keys_pressed, yellow, VEL):
  if keys_pressed[pygame.K_a] and yellow.x - VEL > 0: #left
    yellow.x -= VEL
  if keys_pressed[pygame.K_d] and yellow.x + yellow.width + VEL < BORDER.x: # right
    yellow.x += VEL
  if keys_pressed[pygame.K_w] and yellow.y - VEL > 0: # up
    yellow.y -= VEL
  if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 10: # down
    yellow.y += VEL

def redMove(keys_pressed, red, VEL):
  if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + 10: #left
    red.x -= VEL
  if keys_pressed[pygame.K_RIGHT] and red.x + red.width + VEL < WIDTH: # right
    red.x += VEL
  if keys_pressed[pygame.K_UP] and red.y - VEL > 0: # up
    red.y -= VEL
  if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 10: # down
    red.y += VEL

def handle_bullets(yellowBullets, redBullets, yellow, red, BULLET_VEL):
  for bullet in yellowBullets:
    bullet.x += BULLET_VEL
    if red.colliderect(bullet):
      pygame.event.post(pygame.event.Event(RED_HIT))
      yellowBullets.remove(bullet)
    elif bullet.x > WIDTH:
      yellowBullets.remove(bullet)


  for bullet in redBullets:
    bullet.x -= BULLET_VEL
    if yellow.colliderect(bullet):
      pygame.event.post(pygame.event.Event(YELLOW_HIT))
      redBullets.remove(bullet)
    elif bullet.x < 0:
      redBullets.remove(bullet)

def draw_winner(text):
  draw_text = WINNER_FONT.render(text, 1, WHITE)
  WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2))
  pygame.display.update()
  pygame.time.delay(5000)

def main():

  VEL = settings[0]
  BULLET_VEL = settings[1]
  SPECIAL_WIDTH = settings[2]
  MAX_BULLETS = settings[3]

  screenState = "menu"

  red = pygame.Rect(675, 250, SPACESHIP_SIZE[0], SPACESHIP_SIZE[1])
  yellow = pygame.Rect(225, 250, SPACESHIP_SIZE[0], SPACESHIP_SIZE[1])

  redBullets = []
  yellowBullets = []

  redAmmo = 2
  yellowAmmo = 2

  redCharge = 0
  yellowCharge = 0

  redHealth = 10
  yellowHealth = 10

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
        if (event.key == pygame.K_q or event.key == pygame.K_e) and len(yellowBullets) < MAX_BULLETS and yellowAmmo - 1 >= 0 and screenState == "game":
          yellowAmmo -= 1
          if yellowCharge >= 7:
            bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 27, 10, SPECIAL_WIDTH)
          else:
            bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
          yellowCharge = 0
          yellowBullets.append(bullet)
          BULLET_FIRE_SOUND.play()

      if event.type == pygame.KEYDOWN:
        if (event.key == pygame.K_SLASH or event.key == pygame.K_RSHIFT) and len(redBullets) < MAX_BULLETS and redAmmo - 1 >= 0 and screenState == "game":
          redAmmo -= 1
          if redCharge >= 7:
            bullet = pygame.Rect(red.x, red.y + red.height//2 - 27, 10, SPECIAL_WIDTH)
          else:
            bullet = pygame.Rect(red.x, red.y + red.height//2 - 2, 10, 5)
          redCharge = 0 
          redBullets.append(bullet)
          BULLET_FIRE_SOUND.play()

      if event.type == pygame.MOUSEBUTTONDOWN:
        if screenState == "menu" and pbx <= mouse[0] <= pbx + bw and pby <= mouse[1] <= pby + bh:
          screenState = "game"
        elif screenState == "menu" and pbx <= mouse[0] <= pbx + bw and pby - bh - 10 <= mouse[1] <= pby - 10:
          for setting in range (0, len(settings)):
            settings[setting] = settingsDefault[setting]

      if event.type == pygame.MOUSEBUTTONDOWN:
        for button in range(1, 5):
          height = (70 * button) - 40
          if screenState == "menu" and bminusx <= mouse[0] <= bminusx + cbw and height <= mouse[1] <= height + cbh:
            if settings[button - 1] - settingsChange[button - 1] >= settingsMin[button - 1]:
              settings[button - 1] -= settingsChange[button - 1]

      if event.type == pygame.MOUSEBUTTONDOWN:
        for button in range(1, 5):
          height = (70 * button) - 40
          if screenState == "menu" and baddx <= mouse[0] <= baddx + cbw and height <= mouse[1] <= height + cbh:
            if settings[button - 1] + settingsChange[button - 1] <= settingsMax[button - 1]:
              settings[button - 1] += settingsChange[button - 1]


      
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_r and screenState == "game":
          run = False
          screenState = "menu"

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_p and screenState == "menu":
          screenState = "game"

      if event.type == RED_HIT:
        redHealth -= 1
        BULLET_HIT_SOUND.play()

      if event.type == YELLOW_HIT:
        yellowHealth -= 1
        BULLET_HIT_SOUND.play()

    winner_text = ""

    if redHealth <= 0:
      winner_text = "Yellow Wins!"
      
    if yellowHealth <= 0:
      winner_text = "Red Wins!"

    if winner_text != "":
      draw_winner(winner_text)
      break

    if redAmmo + RELOAD_SPEED/FPS <= MAX_AMMO and screenState == "game":
      redAmmo += RELOAD_SPEED/FPS

    elif redCharge + (RELOAD_SPEED*2)/FPS <= MAX_CHARGE and screenState == "game":
      redCharge += (RELOAD_SPEED*2)/FPS

    if yellowAmmo + RELOAD_SPEED/FPS <= MAX_AMMO and screenState == "game":
      yellowAmmo += RELOAD_SPEED/FPS
    
    elif yellowCharge + (RELOAD_SPEED*2)/FPS <= MAX_CHARGE and screenState == "game":
      yellowCharge += (RELOAD_SPEED*2)/FPS

    
    
    if screenState == "game":
      keys_pressed = pygame.key.get_pressed()
      yellowMove(keys_pressed, yellow, VEL)
      redMove(keys_pressed, red, VEL)


    handle_bullets(yellowBullets, redBullets, yellow, red, BULLET_VEL)

    drawWindow(red, yellow, redBullets, yellowBullets, redHealth, yellowHealth, redAmmo, yellowAmmo, redCharge, yellowCharge, screenState, mouse, settingsNAme, settings, VEL)

  main()


if __name__ == "__main__":
  main()
from Components.settings import *


class Bullet:
  def __init__(self, x, y, direction:[-1 or 1]):
    """direction is 1 or -1 (1 is to the right and -1 is to the left)"""
    self.x = x
    self.y = y
    self.width = BULLET_WIDTH
    self.height = BULLET_HEIGHT
    self.speed = BULLET_VEL * direction
    self.update()
  
  def move(self):
    self.x += self.speed
    self.update()
    
  def update(self):
    self.rect = (self.x, self.y, self.width, self.height)
  
class Bullets:
  def __init__(self):
    self.bullets = []

  def __call__(self):
    return self.bullets
  
  def add_bullet(self, bullet):
    if type(bullet) == Bullet:
      self.bullets.append(bullet)
    else:
      raise ValueError("bullet should be type bullet")
  
  def unpack(self):
    return [(bullet.x, bullet.y) for bullet in self.bullets]
  
  def get_bullets(self):
    return self.unpack()

from typing import Any


class Bullet:
  def __init__(self, x, y, width, height, speed):
    pass
  
  def move(self):
    pass
  
class Bullets:
  def __init__(self, width, height, speed):
    self.bullets = []

  def __call__(self):
    return self.bullets
  
  def add_bullet(self, bullet):
    pass
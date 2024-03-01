import pygame

import map.variable as vari

pygame.init()

class Coordinate:
  def __init__(self):
    self.x = 0
    self.y = 0
    self.on_screen_x = 0
    self.on_screen_y = 0

  def update(self, x, y):
    self.x = x
    self.y = y

  def get_x(self):
    return self.x

  def get_y(self):
    return self.y

  def get_on_screen_x(self):
    return self.on_screen_x

  def get_on_screen_y(self):
    return self.on_screen_y

  def set_x(self, x):
    self.x = x

  def set_y(self, y):
    self.y = y

  def set_on_screen_x(self, x):
    self.on_screen_x = x

  def set_on_screen_y(self, y):
    self.on_screen_y = y
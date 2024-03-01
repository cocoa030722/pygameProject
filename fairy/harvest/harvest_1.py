import pygame

import fairy.fairy_asset as fairy_asset
import fairy.fairy_origin as fairy_origin

pygame.init()

class Fairy(fairy_origin.Origin):
  def __init__(self):
    fairy_origin.Origin.__init__(self)
    self.image=fairy_asset.fairy_image
    self.rect=self.image.get_rect()
    self.rect.x=0
    self.rect.y=0

  def move(self, x, y):
    self.rect.x=x
    self.rect.y=y

  def update(self):
    super().update()
    
    
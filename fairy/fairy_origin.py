import pygame
import random

import fairy.fairy_asset as fairy_asset
import map.variable as vari
pygame.init()


class Origin(pygame.sprite.Sprite):
  # Constructor. Pass in the color of the block,
  # and its x and y position
  def __init__(self):
     # Call the parent class (Sprite) constructor
    pygame.sprite.Sprite.__init__(self)

    self.image=fairy_asset.fairy_image

    self.rect = self.image.get_rect()
    self.rect.x=0
    self.rect.y=0
    self.tile_x=0
    self.tile_y=0
  def update(self):
    pygame.sprite.Sprite.update(self)
    if self.rect.x<vari.SCREEN_WIDTH and self.rect.y<vari.SCREEN_HEIGHT:
      self.rect.x+=16
      self.tile_x+=1
    elif self.rect.x>=vari.SCREEN_WIDTH and self.rect.y<vari.SCREEN_HEIGHT:
      self.rect.x=0
      self.tile_x=0
      self.rect.y+=16
      self.tile_y+=1
    elif self.rect.y>=vari.SCREEN_HEIGHT:
      self.rect.x=0
      self.tile_x=0
      self.rect.y=0
      self.tile_y=0
    
  
  def draw(self, screen):
    screen.blit(self.image, (self.rect.x, self.rect.y))
import pygame

import machine.machine_asset as machine_asset


pygame.init()


class Origin(pygame.sprite.Sprite):
  # Constructor. Pass in the color of the block,
  # and its x and y position
  def __init__(self, x, y):
     # Call the parent class (Sprite) constructor
    pygame.sprite.Sprite.__init__(self)
    self.image=machine_asset.machine_mill_image
    self.rect = self.image.get_rect()
    self.rect.x=x
    self.rect.y=y
    
  def update(self):
    pygame.sprite.Sprite.update(self)
    

  def draw(self, screen):
    screen.blit(self.image, (self.rect.x, self.rect.y))
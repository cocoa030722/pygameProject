import pygame

import ingame_menu.ingame_menu_asset as ingame_menu_asset

pygame.init()

class Item(pygame.sprite.Sprite):
  # Constructor. Pass in the color of the block,
  # and its x and y position
  def __init__(self):
     # Call the parent class (Sprite) constructor
    pygame.sprite.Sprite.__init__(self)
    self.name='empty'
    self.image=ingame_menu_asset.empty_img
    
    self.rect = self.image.get_rect()
    self.normal_item=False #실체가 있는 아이템인지 여부
    self.selling_price=0
    self.buying_price=0
  def create(self):
    self.__init__()

  def update(self):
    pygame.sprite.Sprite.update(self)

  def draw(self, screen):
    screen.blit(self.image, (self.rect.x, self.rect.y))
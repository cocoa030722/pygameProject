import pygame

import item.seed_folder.seed_asset as seed_asset
import item.item_origin as item_origin

pygame.init()


class Item(item_origin.Origin):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.name='berry_seed'
    self.image=seed_asset.berry_seed_image
    
    self.rect = self.image.get_rect()
    self.normal_item=True
    self.buying_price=50
    self.selling_price=25
  def create(self):
    self.__init__()
    
    
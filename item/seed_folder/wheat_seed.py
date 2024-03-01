import pygame

import item.seed_folder.seed_asset as seed_asset
import item.item_origin as item_origin

pygame.init()


class Item(item_origin.Origin):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.name='wheat_seed'
    self.image=seed_asset.wheat_seed_image
    self.rect = self.image.get_rect()
    self.normal_item=True
    self.buying_price=5
    self.selling_price=2
    
  def create(self):
    self.__init__()
    
    
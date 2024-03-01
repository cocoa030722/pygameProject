import pygame

import item.seafood.seafood_asset as seafood_asset
import item.item_origin as item_origin

pygame.init()

class Item(item_origin.Origin):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image=seafood_asset.crucian_image
    self.name='seafood_crucian'
    self.rect = self.image.get_rect()
    self.normal_item=True
    self.buying_price=150
    self.selling_price=300
  def create(self):
    self.__init__()
    
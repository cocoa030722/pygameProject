import pygame

import item.processed.processed_asset as processed_asset
import item.item_origin as item_origin

pygame.init()

class Item(item_origin.Origin):
  def __init__(self):
     # Call the parent class (Sprite) constructor
    pygame.sprite.Sprite.__init__(self)
    self.image=processed_asset.wheat_flour_image
    self.name='wheat_flour'
    self.rect = self.image.get_rect()
    self.normal_item=True #실체가 있는 아이템인지 여부
    self.buying_price=200
    self.selling_price=100
  def create(self):
    self.__init__()
    
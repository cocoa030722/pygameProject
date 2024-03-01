import pygame

import item.harvest.harvest_asset as harvest_asset
import item.item_origin as item_origin

pygame.init()

class Item(item_origin.Origin):
  # Constructor. Pass in the color of the block,
  # and its x and y position
  def __init__(self):
     # Call the parent class (Sprite) constructor
    pygame.sprite.Sprite.__init__(self)
    self.image=harvest_asset.wheat_harvest_image
    self.name='wheat_harvest'
    self.rect = self.image.get_rect()
    self.normal_item=True #실체가 있는 아이템인지 여부
    self.buying_price=20
    self.selling_price=10
  def create(self):
    self.__init__()
    
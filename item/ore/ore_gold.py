import pygame

import item.ore.ore_asset as ore_asset
import item.item_origin as item_origin

pygame.init()

class Item(item_origin.Origin):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image=ore_asset.gold_image
    self.name='gold'
    self.rect = self.image.get_rect()
    self.normal_item=True
    self.buying_price=500
    self.selling_price=1000
    
    #self.stack_size=1
    #self.stack_num=1
    #self.use_time=0
  
  def create(self):
    self.__init__()
    
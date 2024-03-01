import pygame

import item.field.field_asset as field_asset
import item.field.field_origin as field_origin

pygame.init()

class Item(field_origin.Origin):
  # Constructor. Pass in the color of the block,
  # and its x and y position
  def __init__(self):
     # Call the parent class (Sprite) constructor
    pygame.sprite.Sprite.__init__(self)
    self.image=field_asset.field_wood_image
    self.name='field_wood'
    self.rect = self.image.get_rect()
    self.normal_item=True #실체가 있는 아이템인지 여부
    self.buying_price=-1
    self.selling_price=-1
    self.pass_able=False
    
  def update(self):
    pygame.sprite.Sprite.update(self)
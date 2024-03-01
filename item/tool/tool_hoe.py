import pygame

import item.tool.tool_asset as tool_asset
import item.tool.tool_origin as tool_origin

pygame.init()

class Item(tool_origin.Origin):
  # Constructor. Pass in the color of the block,
  # and its x and y position
  def __init__(self):
     # Call the parent class (Sprite) constructor
    pygame.sprite.Sprite.__init__(self)
    self.name='tool_hoe'
    self.image=tool_asset.tool_hoe_image
    
    self.rect = self.image.get_rect()
    self.normal_item=True #실체가 있는 아이템인지 여부
    self.plow_able=True
    self.harvest_able=False
    self.fishing_able=False
    self.mining_able=False
    self.buying_price=100
    self.selling_price=0
  def update(self):
    pygame.sprite.Sprite.update(self)

    

  def draw(self, screen):
    screen.blit(self.image, (self.rect.x, self.rect.y))
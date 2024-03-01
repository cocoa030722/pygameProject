import pygame

import item.tool.tool_asset as tool_asset

pygame.init()

class Origin(pygame.sprite.Sprite):
  # Constructor. Pass in the color of the block,
  # and its x and y position
  def __init__(self, x, y):
     # Call the parent class (Sprite) constructor
    pygame.sprite.Sprite.__init__(self)
    self.image=tool_asset.tool_hoe_image
    
    self.rect = self.image.get_rect()
    self.normal_item=True #실체가 있는 아이템인지 여부
    self.rect.x=x
    self.rect.y=y
    
  def update(self):
    pygame.sprite.Sprite.update(self)

    

  def draw(self, screen):
    screen.blit(self.image, (self.rect.x, self.rect.y))
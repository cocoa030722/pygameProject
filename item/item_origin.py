import pygame

import item.item_origin_asset as item_origin_asset

pygame.init()

class Origin(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image=item_origin_asset.default_image
    self.rect = self.image.get_rect()
    self.normal_item=True #실체가 있는 아이템인지 여부
    

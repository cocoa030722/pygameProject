import pygame

import item.seed_folder.seed_asset as seed_asset
import item.item_origin as item_origin

pygame.init()

class Origin(item_origin.Origin):
  # Constructor. Pass in the color of the block,
  # and its x and y position
  def __init__(self):
     # Call the parent class (Sprite) constructor
    pygame.sprite.Sprite.__init__(self)
    self.image=seed_asset.wheat_seed_image
    
    self.rect = self.image.get_rect()
    self.normal_item=True #실체가 있는 아이템인지 여부

    
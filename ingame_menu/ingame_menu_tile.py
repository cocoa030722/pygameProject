import pygame

import ingame_menu.ingame_menu_asset as ingame_menu_asset
import ingame_menu.empty as empty

pygame.init()

class Tile(pygame.sprite.Sprite):
  # Constructor. Pass in the color of the block,
  # and its x and y position
  def __init__(self, order, x, y):
    # Call the parent class (Sprite) constructor
    pygame.sprite.Sprite.__init__(self)
    self.name='ingame_menu_tile'
    self.image=ingame_menu_asset.inventory_menu_sole_img
    
    self.rect = self.image.get_rect()
    self.rect.x=x
    self.rect.y=y
    self.include_item=empty.Item()
    self.include_item_count=0
    self.order=order
    self.myFont=pygame.font.SysFont('neodgm.ttf', 16)
    

  def update(self, item_name, inventory):
    pygame.sprite.Sprite.update(self)
    if item_name in inventory.inventory:
      self.include_item=(inventory.inventory[item_name]['item'])
      self.include_item_count=(inventory.inventory[item_name]['count'])
    else:
      self.remove()
   
  def add(self, item_name, inventory):
    self.include_item=(inventory.inventory[item_name]['item'])
    self.include_item_count=(inventory.inventory[item_name]['count'])
    
  def remove(self):
    self.include_item=empty.Item()
    self.include_item_count=0
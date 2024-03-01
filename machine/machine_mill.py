import pygame

import machine.machine_asset as machine_asset
import machine.machine_origin as machine_origin

pygame.init()


class Machine(machine_origin.Origin):
  # Constructor. Pass in the color of the block,
  # and its x and y position
  def __init__(self, x, y):
     # Call the parent class (Sprite) constructor
    pygame.sprite.Sprite.__init__(self)
    super().__init__(x, y)
    self.name='mill'
    self.image=machine_asset.machine_mill_image
    
    self.rect = self.image.get_rect()
    self.rect.x=x
    self.rect.y=y
    self.input_item=['wheat_harvest']
    self.input_slot=pygame.sprite.Group()
    self.output_item=['wheat_flour']
    self.output_slot=pygame.sprite.Group()
    self.byproduct_item=['']
    self.byproduct_slot=pygame.sprite.Group()
    
    
  def update(self, pc_inventory):
    pygame.sprite.Sprite.update(self)
    if pc_inventory.picked_item.name in self.input_item:
      pc_inventory.item_count[pc_inventory.picked_item.name]-=1
      
      self.input_item.remove(pc_inventory.picked_item.name)
      self.output_item.append(pc_inventory.picked_item.name)
      pc_inventory.picked_item.remove()
      
  def draw(self, screen):
    screen.blit(self.image, (self.rect.x, self.rect.y))
    for i in self.input_slot:
      screen.blit(i.image, (self.rect.x, self.rect.y))
    for i in self.output_slot:
      screen.blit(i.image, (self.rect.x+16, self.rect.y))
    for i in self.byproduct_slot:
      screen.blit(i.image, (self.rect.x+32, self.rect.y))
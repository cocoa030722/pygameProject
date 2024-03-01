import pygame

import function_object.asset as asset

pygame.init()

class Shipping_box(pygame.sprite.Sprite):
  def __init__(self, x, y, pc_inventory):
    pygame.sprite.Sprite.__init__(self) #필수 요소
    self.x=x
    self.y=y
    self.image=asset.shipping_box_image
    self.rect=self.image.get_rect()
    self.rect.x=x
    self.rect.y=y
    self.name='shipping_box'
    self.item_group=pygame.sprite.Group()
    self.today=0
    self.pc_inventory=pc_inventory
    
  def update(self, dayManager, mapManager):
    if self.today!=dayManager.total_day:
      self.today=dayManager.total_day
      for i in self.item_group:
        self.pc_inventory.money+=i.selling_price
        self.item_group.remove(i)
    self.rect.x=self.x-mapManager.cur_map.on_screen_x
    self.rect.y=self.y-mapManager.cur_map.on_screen_y
    
  def draw(self, screen):
    screen.blit(self.image, (self.rect.x, self.rect.y))
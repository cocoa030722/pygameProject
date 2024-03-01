import pygame

import crop_folder.crop_tile as crop_tile

pygame.init()

class Origin(pygame.sprite.Sprite):
  def __init__(self, x, y, total_day):
    pygame.sprite.Sprite.__init__(self)
    self.crop_seed=crop_tile.wheat_seed_image
    self.crop_harvest=crop_tile.wheat_harvest_image
    self.crop_total=[self.crop_seed, self.crop_harvest]
    self.crop_state=0
    self.image=self.crop_total[self.crop_state]
    self.crop_time=total_day
    self.harvest_able=False
    self.x=x
    self.y=y
    self.rect = self.image.get_rect()
    self.rect.x=x
    self.rect.y=y
    
  def update(self, dayManager, mapManager):
    
    if dayManager.total_day-self.crop_time>=2:
      self.crop_state=1
    if self.crop_state==1:
      self.harvest_able=True
      
    self.image=self.crop_total[self.crop_state]
    self.rect.x=self.x-mapManager.cur_map.on_screen_x
    self.rect.y=self.y-mapManager.cur_map.on_screen_y

  def draw(self, screen):
    screen.blit(self.image, (self.rect.x, self.rect.y))
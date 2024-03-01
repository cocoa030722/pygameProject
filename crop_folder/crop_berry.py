import pygame

import crop_folder.crop_tile as crop_tile
import crop_folder.crop_origin as crop_origin

pygame.init()


class Crop(crop_origin.Origin):
  def __init__(self, x, y, total_day):
    super().__init__(x, y, total_day)
    self.name='berry'
    self.crop_seed=crop_tile.berry_seed_image
    self.crop_harvest=crop_tile.berry_harvest_image
    self.crop_total=[self.crop_seed, self.crop_harvest]
    self.image=self.crop_total[self.crop_state]
    
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
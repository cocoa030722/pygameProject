import pygame

import map.building.building_asset as building_asset
import map.tile.building_house_celling as building_house_celling
import map.tile.building_house_wall as building_house_wall
import map.map_mountain_1 as map_mountain_1
import map.variable as vari

pygame.init()

class Origin(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.x=x
    self.y=y
    self.include_tile=pygame.sprite.Group()
    self.destination='invaild_map'
      
  def draw(self, screen, on_screen_x, on_screen_y):
    for i in self.include_tile:
      screen.blit(i.image, (i.rect.x-on_screen_x, i.rect.y-on_screen_y))
import pygame

import map.building.building_asset as building_asset
import map.tile.building_house_celling as building_house_celling
import map.tile.building_house_wall as building_house_wall
import map.variable as vari

pygame.init()

class Origin(pygame.sprite.Sprite): #정상적 스프라이트로 인식하지 못하고 있음
  def __init__(self, x, y):
    self.x=x
    self.y=y
    self.rect_x=x
    self.rect_y=y
    self.include_tile=pygame.sprite.Group()
    self.include_door=pygame.sprite.Group()
    self.tile_pack={'building_house_celling':building_house_celling, 
                    'building_house_wall':building_house_wall
                    }
  def update(self, mapManager): #메인 로직에 연결해야 함
    self.rect_x=self.x-mapManager.cur_map.on_screen_x
    self.rect_y=self.y-mapManager.cur_map.on_screen_y
  
  def draw(self, screen):
    for i in self.include_tile:
      screen.blit(i.image, (self.rect_x+i.rect.x, self.rect_y+i.rect.y))
    for i in self.include_door:
      screen.blit(i.image, (self.rect_x+i.rect.x, self.rect_y+i.rect.y))
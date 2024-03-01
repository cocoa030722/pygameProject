import pygame
import random

import map.map_draw as map_draw
import map.map_origin as map_origin
import map.tile.river_water_1_tile as river_water_1_tile
import map.tile.river_ground_1_tile as river_ground_1_tile
import map.tile.mountain_ground_1_tile as mountain_ground_1_tile
import map.variable as vari
import map.building.pc_house as pc_house

pygame.init()

class Map(map_origin.Map_origin):
  def __init__(self):
    super().__init__()
    self.next_map_name=['map_river_2', 'map_river_2', 'map_river_2', 'map_river_2']
    self.name='pc_house'

    self.tile_pack={'river_water_1_tile':river_water_1_tile, 
                    'river_ground_1_tile':river_ground_1_tile,
                   }

    self.include_tile=pygame.sprite.Group()
    #전체 맵의 크기
    self.map_width=(vari.SCREEN_WIDTH)
    self.map_height=(vari.SCREEN_HEIGHT//10*9)
    
    #화면의 좌표
    self.on_screen_x=0
    self.on_screen_y=0
    
    for i in range(0,self.map_width,vari.BLOCK):
      for j in range(0,self.map_height,vari.BLOCK):
        if ((i//vari.BLOCK>=8) and (i//vari.BLOCK<=16)) or ((j//vari.BLOCK>=8) and (j//vari.BLOCK<=16)):
          new_tile=self.tile_pack['river_water_1_tile'].Tile()
          new_tile.loc_define(i, j)
          self.include_tile.add(new_tile)
        else:
          new_tile=self.tile_pack['river_ground_1_tile'].Tile()
          new_tile.loc_define(i, j)
          self.include_tile.add(new_tile)
    self.include_building.add(pc_house.Building(5*vari.BLOCK, 5*vari.BLOCK))
    for i in self.include_building:
      print('house location:', i.x, i.y)
  def draw_map(self, screen):
    map_draw.map_draw(self, screen)

    
  def update(self):
    self.include_npc.update()
    self.cropManager.update()

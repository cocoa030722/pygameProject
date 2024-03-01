import pygame
import random

import map.map_draw as map_draw
import map.map_origin as map_origin
import map.tile.mountain_ground_1_tile as mountain_ground_1_tile
import map.tile.mountain_ground_2_tile as mountain_ground_2_tile
import map.variable as vari

pygame.init()

class Map(map_origin.Map_origin):
  def __init__(self, pc_inventory):
    super().__init__()
    self.next_map_name=['map_mountain_2', 'map_river_1', 'invalid_map', 'invalid_map']
    self.name='map_mountain_1'
    self.npcManager.add('gosegu', 5*vari.BLOCK, 5*vari.BLOCK)

    self.tile_pack={'mountain_ground_1_tile':mountain_ground_1_tile, 
                    'mountain_ground_2_tile':mountain_ground_2_tile
                   }

    self.include_tile=pygame.sprite.Group()
    #전체 맵의 크기
    self.map_width=(vari.SCREEN_WIDTH)*2
    self.map_height=(vari.SCREEN_HEIGHT//10*9)*2

    #화면의 좌표
    self.on_screen_x=0
    self.on_screen_y=0

    for i in range(0,self.map_width,vari.BLOCK):
      for j in range(0,self.map_height,vari.BLOCK):
        if (i//vari.BLOCK>=8) and (i//vari.BLOCK<=16):
          new_tile=self.tile_pack['mountain_ground_1_tile'].Tile(i, j)
          self.include_tile.add(new_tile)
        else:
          new_tile=self.tile_pack['mountain_ground_2_tile'].Tile(i, j)
          self.include_tile.add(new_tile)
        
  def draw_map(self, screen):
    map_draw.map_draw(self, screen)
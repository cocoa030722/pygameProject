import pygame
import random

import map.map_draw as map_draw
import map.map_origin as map_origin

import map.tile.field_plain_tile as field_plain_tile
import map.tile.field_gravel_tile as field_gravel_tile

import map.variable as vari

pygame.init()


class Map(map_origin.Map_origin):
  def __init__(self, pc_inventory):
    super().__init__()
    self.next_map_name=['map_field_3', 'invalid_map', 'map_field_1', 'map_river_2']
    self.name='map_field_2'
    self.npcManager.add('ina', 5*vari.BLOCK, 5*vari.BLOCK)

    self.tile_pack={'field_plain_tile':field_plain_tile, 
                    'field_gravel_tile':field_gravel_tile
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
        if random.random()>0.5:
          new_tile=self.tile_pack['field_plain_tile'].Tile(i, j)
          self.include_tile.add(new_tile)
        else:
          new_tile=self.tile_pack['field_gravel_tile'].Tile(i, j)
          self.include_tile.add(new_tile)
          
  def draw_map(self, screen):
    map_draw.map_draw(self, screen)
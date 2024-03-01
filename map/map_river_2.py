import pygame
import random

import function_object.shipping_box as shipping_box
import map.map_draw as map_draw
import map.map_origin as map_origin
import map.tile.river_water_1_tile as river_water_1_tile
import map.tile.river_ground_1_tile as river_ground_1_tile
import map.tile.mountain_ground_1_tile as mountain_ground_1_tile
import map.variable as vari
import item.field.field_wood as field_wood
import map.building.pc_house as pc_house

pygame.init()

class Map(map_origin.Map_origin):
  def __init__(self, pc_inventory):
    super().__init__()
    self.next_map_name=['map_river_3', 'map_field_2', 'map_river_1', 'map_mountain_2']
    self.name='map_river_2'

    self.tile_pack={'river_water_1_tile':river_water_1_tile, 
                    'river_ground_1_tile':river_ground_1_tile,
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
        if ((i//vari.BLOCK>=8) and (i//vari.BLOCK<=16)) or ((j//vari.BLOCK>=8) and (j//vari.BLOCK<=16)):
          new_tile=self.tile_pack['river_water_1_tile'].Tile(i, j)
          self.include_tile.add(new_tile)
        else:
          new_tile=self.tile_pack['river_ground_1_tile'].Tile(i, j)
          self.include_tile.add(new_tile)

    building=pc_house.Building(5*vari.BLOCK, 5*vari.BLOCK)
    if isinstance(building, pygame.sprite.Sprite): #building이 정상적인 스프라이트로 취급되지 않는 문제
      print("legal sprite")
    else:
      print("illegal sprite")
      print(building)
    self.include_building.append(building)
    
    box=shipping_box.Shipping_box(3*vari.BLOCK, 3*vari.BLOCK, pc_inventory)
    self.include_object.add(box)
    ''' 이 형태는 작동하지 않음(변수 범위 문제?)
    self.include_object.add(shipping_box.Shipping_box(3*vari.BLOCK, 3*vari.BLOCK, pc_inventory))
    '''
    
  def draw_map(self, screen):
    map_draw.map_draw(self, screen)
    
    

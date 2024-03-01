import pygame

import map.building.building_origin as building_origin
import map.door.door as door
import map.tile.building_house_celling as building_house_celling
import map.tile.building_house_wall as building_house_wall
import map.map_mountain_1 as map_mountain_1
import map.variable as vari

pygame.init()

class Building(building_origin.Origin):
  def __init__(self, x, y):
    super().__init__(x, y)
    self.include_tile=pygame.sprite.Group()
    self.tile_pack={'building_house_celling':building_house_celling, 
                    'building_house_wall':building_house_wall
                    }
    for i in range(0,5*vari.BLOCK, vari.BLOCK):
      for j in range(0,4*vari.BLOCK, vari.BLOCK):
        if j==0*vari.BLOCK:
          new_tile=self.tile_pack['building_house_celling'].Tile(i, j)
          self.include_tile.add(new_tile)
        
        else:
          new_tile=self.tile_pack['building_house_wall'].Tile(i, j)
          self.include_tile.add(new_tile)
    self.include_door.add(door.Door(2*vari.BLOCK, 3*vari.BLOCK, 'map_mountain_1'))
    
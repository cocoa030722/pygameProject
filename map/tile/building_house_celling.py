import pygame

import map.building.building_asset as building_asset
import map.tile.origin_tile as origin_tile

pygame.init()

class Tile(origin_tile.Origin):
  def __init__(self, x, y):
    super().__init__(x, y)
    self.name='building_house_ceiling'
    self.image=building_asset.house_ceiling
    self.tile_type=['house', 'celling']
    self.is_this_tile={'pass_able': False,
                      'sowing_able': False,
                      }
    self.rect = self.image.get_rect()
    self.rect.x=x
    self.rect.y=y

import pygame

import map.tile.tile_asset as tile_asset
import map.tile.origin_tile as origin_tile

pygame.init()

class Tile(origin_tile.Origin):
  # Constructor. Pass in the color of the block,
  # and its x and y position
  def __init__(self, x, y):
    super().__init__(x, y)
    self.name='wall_1_tile'
    self.tile_type=['wall']
    self.image=tile_asset.wall_1
    self.is_this_tile={'pass_able': False,
                      'sowing_able': False,
                      }
    self.rect = self.image.get_rect()
    self.rect.x=x
    self.rect.y=y
  

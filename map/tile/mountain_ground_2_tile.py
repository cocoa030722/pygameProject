import pygame

import map.tile.tile_asset as tile_asset
import map.tile.origin_tile as origin_tile

pygame.init()

class Tile(origin_tile.Origin):
  def __init__(self, x, y):
    super().__init__(x, y)
    self.name='mountain_ground_2_tile'
    self.tile_type=['mountain', 'ground']
    self.image=tile_asset.mountain_ground_2
    self.is_this_tile={'pass_able': True,
                      'sowing_able': False,
                      }
    self.pass_able=True
    self.sowing_able=False
    self.rect = self.image.get_rect()
    self.rect.x=x
    self.rect.y=y
    
import pygame

import map.tile.tile_asset as tile_asset

pygame.init()

class Origin(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.name='origin'
    self.image=tile_asset.field_plain
    self.is_this_tile={'pass_able': True,
                       'sowing_able': False,
                      }
    self.x=x
    self.y=y
    self.rect = self.image.get_rect()
    self.rect.x=x
    self.rect.y=y
  
  def update(self, mapManager):
    self.rect.x=self.x-mapManager.cur_map.on_screen_x
    self.rect.y=self.y-mapManager.cur_map.on_screen_y

  def draw(self, screen):
    screen.blit(self.image, (self.rect.x, self.rect.y))
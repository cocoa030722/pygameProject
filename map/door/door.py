import pygame

import map.door.door_asset as door_asset
import map.door.door_origin as door_origin
import map.tile.building_house_celling as building_house_celling
import map.tile.building_house_wall as building_house_wall
import map.variable as vari

pygame.init()

class Door(door_origin.Origin):
  def __init__(self, x, y, destination):
    pygame.sprite.Sprite.__init__(self)
    self.x=x
    self.y=y
    self.include_tile=pygame.sprite.Group()
    self.destination=destination
    self.image=door_asset.door_image
    self.rect=self.image.get_rect()
    self.rect.x=self.x
    self.rect.y=self.y
    
  def draw(self, screen, on_screen_x, on_screen_y):
    screen.blit(self.image, (self.rect.x-on_screen_x, self.rect.y-on_screen_y))
    
      
    
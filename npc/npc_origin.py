import pygame

import npc.npc_tile as npc_tile


pygame.init()

class Npc_origin(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.x = x
    self.y = y
    self.img=pygame.Surface.subsurface(npc_tile.npc_raw1, (0,16,12,14))
    self.img=pygame.transform.scale(self.img, (16,16))
    self.rect=self.img.get_rect()
    self.rect.x=self.x
    self.rect.y=self.y

  def update(self, mapManager):
    self.rect.x=self.x-mapManager.cur_map.on_screen_x
    self.rect.y=self.y-mapManager.cur_map.on_screen_y
    
  def draw(self, screen):
    screen.blit(self.img, (self.rect.x, self.rect.y))

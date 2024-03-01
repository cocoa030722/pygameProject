import pygame

import map.variable as vari

def map_draw(self, screen): # 경게선 내에 있는지 여부를 판단하지 않고 출력함(이게 최선인가?)
  for i in self.include_tile:
    i.draw(screen)

  self.npcManager.draw(screen)

  for i in self.include_field_item:
    i.draw(screen, self.on_screen_x, self.on_screen_y)

  self.cropManager.draw(screen)

  for i in self.include_object:
    i.draw(screen)
      
  for i in self.include_building:
    i.draw(screen)
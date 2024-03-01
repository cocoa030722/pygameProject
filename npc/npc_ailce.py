import pygame

import npc.neighbor_origin as neighbor_origin
import npc.npc_tile as npc_tile
import map.variable as vari

pygame.init()

class Npc(neighbor_origin.Neighbor):
  def __init__(self, x, y):
    super().__init__(x, y)
    self.image=npc_tile.npc_ailce
    self.image=pygame.transform.scale(self.image, (vari.BLOCK,vari.BLOCK))
    self.standing=npc_tile.ailce_standing
    self.rect=self.image.get_rect()
    self.rect.left=self.x
    self.rect.top=self.y
    self.name='ailce'
    self.enemy=['miko'] #본인의 관계도를 올릴 시 자동으로 관계도가 감소하는 npc
    self.ownership=['map_field_1']

    

import pygame

import npc.npc_tile as npc_tile
import npc.action.attack as act_attack
import npc.action.blame as act_blame
import npc.action.praise as act_praise
import npc.neighbor_origin as neighbor_origin
import map.variable as vari

pygame.init()

class Npc(neighbor_origin.Neighbor):
  def __init__(self, x, y):
    super().__init__(x, y)
    self.image=npc_tile.npc_chris
    self.image=pygame.transform.scale(self.image, (vari.BLOCK,vari.BLOCK))
    self.standing=npc_tile.chris_standing
    self.rect=self.image.get_rect()
    self.rect.left=self.x
    self.rect.top=self.y
    self.name='chris'
    self.enemy=['pekora']
    self.ownership=['map_river_1']
   
    

import pygame

import npc.action.attack as act_attack
import npc.action.blame as act_blame
import npc.action.praise as act_praise
import npc.action.land_purchase as act_land_purchase
import npc.npc_origin as npc_origin
import npc.npc_tile as npc_tile
import map.variable as vari

pygame.init()

#경쟁자들의 원형
class Neighbor(npc_origin.Npc_origin):
  def __init__(self, x, y):
      super().__init__(x, y)
      self.image=npc_tile.npc_ailce
      self.image=pygame.transform.scale(self.image, (vari.BLOCK,vari.BLOCK))
      self.standing=npc_tile.ailce_standing
      self.rect=self.image.get_rect()
      self.rect.x=self.x
      self.rect.y=self.y
      self.name='ailce'
      self.enemy=['miko'] #본인의 관계도를 올릴 시 자동으로 관계도가 감소하는 npc
      self.reputation=0
      self.ownership=['map_field_1']
      self.choice_list=[act_praise, act_blame]
    
  def update(self, mapManager):
    self.rect.x=self.x-mapManager.cur_map.on_screen_x
    self.rect.y=self.y-mapManager.cur_map.on_screen_y

    if self.reputation>=1000 and (act_land_purchase not in self.choice_list):
      self.choice_list.append(act_land_purchase)
    if self.reputation<=-1000 and (act_attack not in self.choice_list):
      self.choice_list.append(act_attack)

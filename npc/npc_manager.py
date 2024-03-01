import pygame

import npc.npc_ailce as npc_ailce
import npc.npc_chris as npc_chris
import npc.npc_gosegu as npc_gosegu
import npc.npc_ina as npc_ina
import npc.npc_laplus as npc_laplus
import npc.npc_miko as npc_miko
import npc.npc_pekora as npc_pekora
import npc.npc_suisei as npc_suisei
import map.variable as vari

pygame.init()

#유일한 npc들의 목록
npc_dic={'ailce': npc_ailce.Npc(5*vari.BLOCK, 5*vari.BLOCK),
     'chris': npc_chris.Npc(5*vari.BLOCK, 5*vari.BLOCK),
     'gosegu': npc_gosegu.Npc(5*vari.BLOCK, 5*vari.BLOCK),
     'ina': npc_ina.Npc(5*vari.BLOCK, 5*vari.BLOCK),
     'laplus': npc_laplus.Npc(5*vari.BLOCK, 5*vari.BLOCK),
     'miko': npc_miko.Npc(5*vari.BLOCK, 5*vari.BLOCK), 
     'pekora': npc_pekora.Npc(5*vari.BLOCK, 5*vari.BLOCK),
     'suisei': npc_suisei.Npc(5*vari.BLOCK, 5*vari.BLOCK)
    }

class Npc_manager:
  def __init__(self):
    
    self.valid_npc={}
    
  def add(self, key, x, y):
    self.valid_npc[key]=npc_dic[key]
    self.valid_npc[key].x=x
    self.valid_npc[key].y=y
    self.valid_npc[key].rect.x=x
    self.valid_npc[key].rect.y=y

  def update(self, mapManager):
    for key in self.valid_npc:
      self.valid_npc[key].update(mapManager)
      
  def draw(self, screen):
    for i in self.valid_npc:
      self.valid_npc[i].draw(screen)
      
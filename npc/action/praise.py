import pygame

import npc.npc_manager as npc_manager


pygame.init()
name='praise'
def act(map, npc, pc):
  print('praise')
  npc.reputation=npc.reputation+100
  for i in npc.enemy:
    npc_manager.npc_dic[i].reputation=npc_manager.npc_dic[i].reputation-100
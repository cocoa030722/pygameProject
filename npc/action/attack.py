import pygame

pygame.init()
name='attack'
def act(map, npc, pc):
  print("attack")
  for i in npc.ownership:
    pc.ownership.append(i)
  map.include_npc.remove(npc)
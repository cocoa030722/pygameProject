import pygame

pygame.init()
name='land_purchase'
def act(map, npc, pc):
  print("land_purchase")
  if pc.inventory.money>50000:
    print('purchasing land')
    pc.inventory.money-=50000 #토지 하나의 가격
    for i in npc.ownership:
      pc.ownership.append(i)
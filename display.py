import pygame

import map.variable as vari
import screen_state

screen = pygame.display.set_mode((vari.SCREEN_WIDTH, vari.SCREEN_HEIGHT))

def draw(essential_pack, pc_object):
  
  screen.fill((255, 255, 255)) #layer 0:화면 초기화
  
  essential_pack['mapManager'].draw(screen) #layer 1:맵

  pc_object.draw(screen) #layer 2:플레이어
  #essential_pack['fairyManager'].draw(screen)
  
  #layer 3:menu
  if screen_state.menu_called:
    essential_pack['ingameMenuManager'].draw(screen)
    essential_pack['menuManager'].draw(screen)
    
  elif screen_state.chat_window_called:
    essential_pack['menuManager'].close()
    essential_pack['chatWindow'].draw(screen, pc_object.npc)
    essential_pack['dayManager'].draw(screen)
    essential_pack['ingame_info_object'].draw(screen)
  else:
    essential_pack['menuManager'].close()
    essential_pack['ingameMenuManager'].draw(screen)
    essential_pack['dayManager'].draw(screen)
    essential_pack['ingame_info_object'].draw(screen)
  
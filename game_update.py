import pygame

import screen_state

pygame.init()

def update(essential_pack, pc_object):
  if screen_state.menu_called:
    essential_pack['menuManager'].update(essential_pack['menuManager'])
  elif screen_state.chat_window_called:
    essential_pack['chatWindow'].update(essential_pack['mapManager'], pc_object)
  else:
    pc_object.update(essential_pack['mapManager'], essential_pack['ingameMenuManager'], essential_pack['dayManager'])
    essential_pack['ingameMenuManager'].update(essential_pack['ingameMenuManager'])
    #essential_pack['fairyManager'].update()

  essential_pack['ingame_info_object'].update()
  essential_pack['mapManager'].update(essential_pack['dayManager'], essential_pack['mapManager'])
  essential_pack['dayManager'].update()
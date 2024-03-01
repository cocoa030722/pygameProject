import pygame

import map.variable as vari

pygame.init()

cursor_raw=pygame.image.load('core/src/main/assets/interfaces/icons.png')


cursor_img=pygame.Surface.subsurface(cursor_raw, (16,16,16,16))

help_menu_rect=pygame.Rect((0, (vari.SCREEN_HEIGHT//10)*9), (vari.SCREEN_WIDTH, vari.SCREEN_HEIGHT//10))

inventory_menu_rect=pygame.Rect((0, (vari.SCREEN_HEIGHT//10)*9), (vari.SCREEN_WIDTH, vari.SCREEN_HEIGHT//10))
inventory_menu_img_raw=pygame.image.load('core/src/main/assets/interfaces/toolbar.png')
inventory_menu_sole_img=pygame.Surface.subsurface(inventory_menu_img_raw, (vari.BLOCK*4, 0, 22, 32))
inventory_menu_sole_img=pygame.transform.scale(inventory_menu_sole_img, (vari.SCREEN_WIDTH//9, vari.SCREEN_WIDTH//9))

empty_img=pygame.Surface.subsurface(inventory_menu_img_raw, (vari.BLOCK*11, vari.BLOCK*0, vari.BLOCK, vari.BLOCK)) 
  
import pygame

import map.variable as vari

pygame.init()

player_raw=pygame.image.load('core/src/main/assets/sprites/shopkeeper.png')
player_img=pygame.Surface.subsurface(player_raw, (0,0,14,16))
player_img=pygame.transform.scale(player_img, (vari.BLOCK,vari.BLOCK))

cursor_raw=pygame.image.load('core/src/main/assets/interfaces/icons.png')
cursor_img=pygame.Surface.subsurface(cursor_raw, (16,16,16,16))

import pygame

import map.variable as vari

pygame.init()

menu_raw=pygame.image.load('core/src/main/assets/interfaces/surface.png')
cursor_raw=pygame.image.load('core/src/main/assets/interfaces/icons.png')
menu_icon_raw=pygame.image.load('core/src/main/assets/interfaces/large_buffs.png')

menu_icon_list=[pygame.Surface.subsurface(menu_icon_raw, (vari.BLOCK*0,vari.BLOCK*0,16,16)),
  pygame.Surface.subsurface(menu_icon_raw, (vari.BLOCK*1,vari.BLOCK*0,16,16)),
  pygame.Surface.subsurface(menu_icon_raw, (vari.BLOCK*6,vari.BLOCK*1,16,16)),
  pygame.Surface.subsurface(menu_icon_raw, (vari.BLOCK*8,vari.BLOCK*0,16,16)),
  pygame.Surface.subsurface(menu_icon_raw, (vari.BLOCK*4,vari.BLOCK*0,16,16)),
 ]

menu_shop_icon_list=[pygame.Surface.subsurface(menu_icon_raw, (vari.BLOCK*5,vari.BLOCK*0,16,16)),
  pygame.Surface.subsurface(menu_icon_raw, (vari.BLOCK*6,vari.BLOCK*0,16,16)),
  pygame.Surface.subsurface(menu_icon_raw, (vari.BLOCK*4,vari.BLOCK*0,16,16)),
 ]

menu_witch_icon_list=[pygame.Surface.subsurface(menu_icon_raw, (vari.BLOCK*1,vari.BLOCK*1,16,16)),
  pygame.Surface.subsurface(menu_icon_raw, (vari.BLOCK*14,vari.BLOCK*0,16,16)),
  pygame.Surface.subsurface(menu_icon_raw, (vari.BLOCK*14,vari.BLOCK*2,16,16)),
  pygame.Surface.subsurface(menu_icon_raw, (vari.BLOCK*4,vari.BLOCK*0,16,16)),
 ]

menu_img=pygame.Surface.subsurface(menu_raw, (0,0,88,128))
menu_img=pygame.transform.scale(menu_img, (vari.SCREEN_WIDTH, vari.SCREEN_HEIGHT))

cursor_img=pygame.Surface.subsurface(cursor_raw, (16,16,16,16))

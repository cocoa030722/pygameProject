import pygame

pygame.init()

tool1=pygame.image.load('core/src/main/assets/sprites/items.png')

tool_hoe_image=pygame.Surface.subsurface(tool1, (13*16,9*16,16,16))
tool_sickel_image=pygame.Surface.subsurface(tool1, (13*16,6*16,16,16))
tool_fishing_rod_image=pygame.Surface.subsurface(tool1, (1*16,4*16,16,16))
tool_pickaxe_image=pygame.Surface.subsurface(tool1, (4*16,29*16,16,16))

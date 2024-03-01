import pygame

pygame.init()

raw1=pygame.image.load('core/src/main/assets/sprites/items.png')

field_wood_image=pygame.Surface.subsurface(raw1, (5*16,6*16,16,16))
field_stone_image=pygame.Surface.subsurface(raw1, (3*16, 9*16,16,16))


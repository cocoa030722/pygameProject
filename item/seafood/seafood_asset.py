import pygame

pygame.init()

raw1=pygame.image.load('core/src/main/assets/sprites/items.png')

crucian_image=pygame.Surface.subsurface(raw1, (0*16,28*16,16,16))


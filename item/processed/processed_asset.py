import pygame

pygame.init()

processed1=pygame.image.load('core/src/main/assets/sprites/items.png')

wheat_flour_image=pygame.Surface.subsurface(processed1, (1*16,29*16,16,16))


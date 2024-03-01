import pygame

pygame.init()

farm1=pygame.image.load('core/src/main/assets/environment/terrain_features.png')

wheat_harvest_image=pygame.Surface.subsurface(farm1, (10*16,0,16,16))
berry_harvest_image=pygame.Surface.subsurface(farm1, (0, 7*16,16,16))


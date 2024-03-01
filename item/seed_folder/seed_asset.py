import pygame

pygame.init()

farm1=pygame.image.load('core/src/main/assets/environment/terrain_features.png')
farm2=pygame.image.load('core/src/main/assets/sprites/items.png')

wheat_seed_image=pygame.Surface.subsurface(farm1, (14*16,0,16,16))
berry_seed_image=pygame.Surface.subsurface(farm2, (0,16*23,16,16))

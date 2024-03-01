import pygame

pygame.init()

tile_house=pygame.image.load('core/src/main/assets/environment/tiles_caves_crystal.png')
tile_shop=pygame.image.load('core/src/main/assets/environment/tiles_caves_crystal.png')
tile_church=pygame.image.load('core/src/main/assets/environment/tiles_caves_crystal.png')

house_wall=pygame.Surface.subsurface(tile_house, (0*16,3*16,16,16))
house_ceiling=pygame.Surface.subsurface(tile_house, (0*16,12*16,16,16))
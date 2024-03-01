import pygame

pygame.init()

tile_door=pygame.image.load('core/src/main/assets/environment/tiles_caves_crystal.png')
tile_portal=pygame.image.load('core/src/main/assets/environment/tiles_caves_crystal.png')

door_image=pygame.Surface.subsurface(tile_door, (8*16,3*16,16,16))
portal_image=pygame.Surface.subsurface(tile_door, (12*16,4*16,16,16))
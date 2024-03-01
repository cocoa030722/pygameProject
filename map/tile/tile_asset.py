import pygame

import map.variable as vari

pygame.init()

tile_field=pygame.image.load('core/src/main/assets/environment/tiles_caves_crystal.png')
tile_river_ground=pygame.image.load('core/src/main/assets/environment/tiles_caves_crystal.png')
tile_river_water=pygame.image.load('core/src/main/assets/environment/water2.png')
tile_mountain=pygame.image.load('core/src/main/assets/environment/tiles_sewers.png')


field_plain=pygame.Surface.subsurface(tile_field, (0,0,16,16))
field_gravel=pygame.Surface.subsurface(tile_field, (16,0,16,16))
celler_ladder=pygame.Surface.subsurface(tile_field, (16,16,16,16))
wall_1=pygame.Surface.subsurface(tile_field, (vari.BLOCK*6,0,16,16))

mountain_ground_1=pygame.Surface.subsurface(tile_mountain, (0,0,16,16))
mountain_ground_2=pygame.Surface.subsurface(tile_mountain, (16,0,16,16))

river_ground_1=pygame.Surface.subsurface(tile_river_ground, (0,0,16,16))
river_water_1=pygame.Surface.subsurface(tile_river_water, (0,0,16,16))
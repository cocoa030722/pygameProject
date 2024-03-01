import pygame

pygame.init()

machine1=pygame.image.load('core/src/main/assets/environment/custom_tiles/weak_floor.png')

machine_mill_image=pygame.Surface.subsurface(machine1, (0,0,16,16))
machine_mill_image=pygame.transform.scale(machine_mill_image, (32, 32))
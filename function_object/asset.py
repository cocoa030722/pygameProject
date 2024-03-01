import pygame

pygame.init()

object_raw=pygame.image.load('core/src/main/assets/sprites/items.png')

shipping_box_image=pygame.Surface.subsurface(object_raw, (5*16,2*16,16,16))
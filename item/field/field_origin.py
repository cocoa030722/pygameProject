import pygame

import item.field.field_asset as field_asset

pygame.init()


class Origin(pygame.sprite.Sprite):
  # Constructor. Pass in the color of the block,
  # and its x and y position
  def __init__(self, x, y):
     # Call the parent class (Sprite) constructor
    pygame.sprite.Sprite.__init__(self)
    
    self.image=field_asset.field_wood_image
    
    self.rect = self.image.get_rect()
    self.rect.x=x
    self.rect.y=y
    self.normal_item=True #실체가 있는 아이템인지 여부
  def update(self):
    pygame.sprite.Sprite.update(self)
    


  def draw(self, screen, on_screen_x, on_screen_y):
    screen.blit(self.image, (self.rect.x-on_screen_x, self.rect.y-on_screen_y))
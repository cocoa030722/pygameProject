import pygame

import pc.asset as asset
import map.variable as vari

pygame.init()

class PlayerFront(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    #전체 맵에서의 좌표
    self.x=0
    self.y=0
    #화면상에서의 좌표는 self.좌표-현재 맵의 좌표
    self.dir=0
    self.pre_dir=0
    self.dir_xy=[[0,1], [-1,0], [0,-1], [1,0]]
    
    self.image=asset.cursor_img
    
    self.rect=self.image.get_rect() # 모든 sprite 는 고유한 rect를 가져야 함
    self.rect.x=self.x+(self.dir_xy[self.dir][0]*vari.BLOCK)
    self.rect.y=self.y+(self.dir_xy[self.dir][1]*vari.BLOCK)
  
  def update(self, x, y, cur_map):
    self.x=x+(self.dir_xy[self.dir][0]*vari.BLOCK)
    self.y=y+(self.dir_xy[self.dir][1]*vari.BLOCK)

    #rect의 표준
    self.rect.x=self.x-cur_map.on_screen_x
    self.rect.y=self.y-cur_map.on_screen_y
    
  def draw(self, screen):
    screen.blit(self.image, (self.rect.x, self.rect.y))
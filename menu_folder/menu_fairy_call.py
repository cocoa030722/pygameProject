import pygame

import menu_folder.menu_asset as menu_asset
import map.variable as vari

pygame.init()

class Menu_fairy_call(pygame.sprite.Sprite): #다수의 변수 열람할 수 있도록 스크롤 기능 추가
  def __init__(self, eventList):
    pygame.sprite.Sprite.__init__(self)
    self.menu_name='Menu_fairy_call'
    self.choice_count=3
    self.menu_icon_list=[pygame.Surface.subsurface(menu_asset.menu_icon_raw, (vari.BLOCK*0,vari.BLOCK*0,16,16)),
      pygame.Surface.subsurface(menu_asset.menu_icon_raw, (vari.BLOCK*1,vari.BLOCK*0,16,16)),
      pygame.Surface.subsurface(menu_asset.menu_icon_raw, (vari.BLOCK*2,vari.BLOCK*0,16,16)),
     ]
    self.menu_icon_list_rect=[self.menu_icon_list[0].get_rect(),
                              self.menu_icon_list[1].get_rect(),
                              self.menu_icon_list[2].get_rect()]

    for i in range(0,self.choice_count):
      self.menu_icon_list_rect[i].left=(int)(vari.SCREEN_WIDTH*(1/10))
      self.menu_icon_list_rect[i].top=(int)(vari.SCREEN_HEIGHT*(1/10))*(i+1)

    self.menu_op_name=['call', 'call', 'call']
    self.menu_op=['Menu_fairy_call', 'Menu_fairy_call', 'Menu_fairy_call']

    self.menu_img=pygame.Surface.subsurface(menu_asset.menu_raw, (0,0,88,128))
    self.menu_img=pygame.transform.scale(self.menu_img, (vari.SCREEN_WIDTH, vari.SCREEN_HEIGHT))
    self.menu_img_rect=self.menu_img.get_rect()
    self.menu_img_rect.left=0
    self.menu_img_rect.top=0

    self.cursor_img=pygame.Surface.subsurface(menu_asset.cursor_raw, (16,16,16,16))
    self.cursor=0
    self.cursor_img_rect=self.cursor_img.get_rect()
    self.cursor_img_rect.left=(int)(vari.SCREEN_WIDTH*(1/10))
    self.cursor_img_rect.top=(int)(vari.SCREEN_HEIGHT*(1/10))+(int)(vari.SCREEN_HEIGHT*(1/10))*self.cursor

    self.load_pack={}
    for i in range(0, self.choice_count):
      self.load_pack[i]=self.menu_op[i]

    self.myFont=pygame.font.Font('Sejong hospital Light.ttf', 8)
    self.eventList=eventList
  def update(self, menuManager):

      for event in self.eventList:
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_DOWN:
            self.cursor=self.cursor+1 if self.cursor+1<self.choice_count else self.choice_count-1
          elif event.key == pygame.K_UP:
            self.cursor=self.cursor-1 if self.cursor-1>0 else 0
          elif event.key == pygame.K_e:
            self.call()

      self.cursor_img_rect.left=(int)(vari.SCREEN_WIDTH*(1/10))
      self.cursor_img_rect.top=(int)(vari.SCREEN_HEIGHT*(1/10))+(int)(vari.SCREEN_HEIGHT*(1/10))*self.cursor

      self.myText=self.myFont.render(self.menu_op_name[self.cursor], True, (255,255,255))

  def call(self):
    print('call')
    
    
  def draw(self, screen):
    screen.fill((0, 0, 0)) #기존의 모든 요소 가리기
    screen.blit(self.menu_img, (0, 0))

    for j in range(0, len(self.menu_icon_list)):
      screen.blit(self.menu_icon_list[j],
          (self.menu_icon_list_rect[j].left, self.menu_icon_list_rect[j].top))
      self.myText=self.myFont.render(self.menu_op_name[self.cursor], True, (255,255,255))
      screen.blit(self.myText, (128, self.menu_icon_list_rect[self.cursor].y))
      
    screen.blit(self.cursor_img, (self.cursor_img_rect.left, self.cursor_img_rect.top))


    
    

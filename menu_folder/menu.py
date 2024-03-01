import pygame

import menu_folder.menu_asset as menu_asset
import map.variable as vari
import screen_state

pygame.init()

class Menu(pygame.sprite.Sprite):
  def __init__(self, eventList):
    pygame.sprite.Sprite.__init__(self)
    self.menu_name='Menu'
    self.choice_count=5
    self.menu_icon_list_rect=[menu_asset.menu_icon_list[0].get_rect(),
                              menu_asset.menu_icon_list[1].get_rect(),
                              menu_asset.menu_icon_list[2].get_rect(),
                              menu_asset.menu_icon_list[3].get_rect(),
                              menu_asset.menu_icon_list[4].get_rect()]

    for i in range(0,self.choice_count):
      self.menu_icon_list_rect[i].left=(int)(vari.SCREEN_WIDTH*(1/10))
      self.menu_icon_list_rect[i].top=(int)(vari.SCREEN_HEIGHT*(1/10))*(i+1)
    
    self.menu_img_rect=menu_asset.menu_img.get_rect()
    self.menu_img_rect.left=0
    self.menu_img_rect.top=0

    self.cursor=0
    self.cursor_img_rect=menu_asset.cursor_img.get_rect()
    self.cursor_img_rect.left=(int)(vari.SCREEN_WIDTH*(1/10))
    self.cursor_img_rect.top=(int)(vari.SCREEN_HEIGHT*(1/10))+(int)(vari.SCREEN_HEIGHT*(1/10))*self.cursor

    self.menu_op_name=['Fairy call', 'Setting', 'shop', 'witch', 'Exit']
    self.menu_op=['Menu_fairy', 'Menu', 'Menu_shop', 'Menu_witch', 'Menu']
    
    self.load_pack={}
    for i in range(0, len(self.menu_op)):
      self.load_pack[i]=self.menu_op[i]
      
    self.myFont=pygame.font.Font('Sejong hospital Light.ttf', 8)
    self.eventList=eventList #오버헤드를 줄이기 위해  main의 리스트를 직접 할당
    
  def update(self, menuManager):
    
    for event in self.eventList:
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
          self.cursor=self.cursor+1 if self.cursor+1<self.choice_count else self.choice_count-1
        elif event.key == pygame.K_UP:
          self.cursor=self.cursor-1 if self.cursor-1>0 else 0
        elif event.key == pygame.K_e:
          if self.cursor!=self.choice_count-1:
            menuManager.change_menu(self.load_pack[self.cursor])
          else:
            screen_state.menu_called=False
            
    self.cursor_img_rect.left=(int)(vari.SCREEN_WIDTH*(1/10))
    self.cursor_img_rect.top=(int)(vari.SCREEN_HEIGHT*(1/10))+(int)(vari.SCREEN_HEIGHT*(1/10))*self.cursor
    
    self.myText=self.myFont.render(self.menu_op[self.cursor], True, (255,255,255))
    
  def draw(self, screen):
    screen.fill((0, 0, 0)) #기존의 모든 요소 가리기
    screen.blit(menu_asset.menu_img, (0, 0))

    for j in range(0, len(menu_asset.menu_icon_list)):
      screen.blit(menu_asset.menu_icon_list[j],
          (self.menu_icon_list_rect[j].left, self.menu_icon_list_rect[j].top))
    screen.blit(menu_asset.cursor_img, (self.cursor_img_rect.left, self.cursor_img_rect.top))
      
    
    self.myText=self.myFont.render(self.menu_op_name[self.cursor], True, (255,255,255))
    screen.blit(self.myText, (128, self.menu_icon_list_rect[self.cursor].y))

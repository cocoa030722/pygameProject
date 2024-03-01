
import pygame

import menu_folder.menu_asset as menu_asset
import map.variable as vari

pygame.init()

class Menu_witch(pygame.sprite.Sprite):
  def __init__(self, eventList):
    pygame.sprite.Sprite.__init__(self)
    self.menu_name='Menu_witch'
    self.menu_icon_list_rect=[menu_asset.menu_witch_icon_list[0].get_rect(),
                              menu_asset.menu_witch_icon_list[1].get_rect(),
                              menu_asset.menu_witch_icon_list[2].get_rect(),
                              menu_asset.menu_witch_icon_list[3].get_rect()]

    for i in range(0,len(self.menu_icon_list_rect)):
      self.menu_icon_list_rect[i].left=(int)(vari.SCREEN_WIDTH*(1/10))
      self.menu_icon_list_rect[i].top=(int)(vari.SCREEN_HEIGHT*(1/10))*(i+1)


    self.menu_op=['Menu_witch', 'Menu_witch', 'Menu_witch', 'Menu']
    self.menu_op_name=['talk', 'quest', 'request', 'exit']
    self.choice_count=len(self.menu_op)
    self.menu_img_rect=menu_asset.menu_img.get_rect()
    self.menu_img_rect.left=0
    self.menu_img_rect.top=0

    self.cursor=0
    self.cursor_img_rect=menu_asset.cursor_img.get_rect()
    self.cursor_img_rect.left=(int)(vari.SCREEN_WIDTH*(1/10))
    self.cursor_img_rect.top=(int)(vari.SCREEN_HEIGHT*(1/10))+(int)(vari.SCREEN_HEIGHT*(1/10))*self.cursor

    self.load_pack={}
    for i in range(0, len(self.menu_op)):
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
          menuManager.change_menu(self.load_pack[self.cursor])
        elif event.key == pygame.K_SPACE:
          print(self.menu_op_name[self.cursor])
          if self.cursor==0:
            self.act()
          elif self.cursor==1:
            self.act()
          elif self.cursor==2:
            print('exit')
          elif self.cursor==3:
            print('exit')

    self.cursor_img_rect.left=(int)(vari.SCREEN_WIDTH*(1/10))
    self.cursor_img_rect.top=(int)(vari.SCREEN_HEIGHT*(1/10))+(int)(vari.SCREEN_HEIGHT*(1/10))*self.cursor

    self.myText=self.myFont.render(self.menu_op_name[self.cursor], True, (255,255,255))

  def act(self):
    print('witch')

  def draw(self, screen):
    screen.fill((0, 0, 0)) #기존의 모든 요소 가리기
    screen.blit(menu_asset.menu_img, (0, 0))

    for j in range(0, len(menu_asset.menu_witch_icon_list)):
      screen.blit(menu_asset.menu_witch_icon_list[j],
        (self.menu_icon_list_rect[j].left, self.menu_icon_list_rect[j].top))
      screen.blit(menu_asset.cursor_img, (self.cursor_img_rect.left, self.cursor_img_rect.top))


    self.myText=self.myFont.render(self.menu_op_name[self.cursor], True, (255,255,255))
    screen.blit(self.myText, (128, self.menu_icon_list_rect[self.cursor].y))

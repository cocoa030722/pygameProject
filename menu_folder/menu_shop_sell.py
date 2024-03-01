import pygame

import menu_folder.menu_asset as menu_asset
import map.variable as vari

pygame.init()

class Menu_shop_sell(pygame.sprite.Sprite):
  def __init__(self, eventList, pc_inventory):
    pygame.sprite.Sprite.__init__(self)
    self.menu_name='Menu_shop_sell'

    self.choice_count=0 #전체 리스트의 길이
    self.show_count=9 #보여줄 리스트의 길이
    self.show_start=0
    self.show_end=self.show_start+self.show_count
    
    self.menu_op_name=[]
    self.menu_op=['Menu_shop_sell', 'Menu_shop_sell', 'Menu_shop_sell']
    self.item_group=pygame.sprite.Group()
    for i in pc_inventory.inventory:
      if i!='empty':
        self.menu_op_name.append(i)
        self.item_group.add(pc_inventory.inventory[i]['item'])
        self.choice_count+=1
    
    self.item_group_list=self.item_group.sprites()
    self.menu_img_rect=menu_asset.menu_img.get_rect()
    self.menu_img_rect.left=0
    self.menu_img_rect.top=0

    self.inner_cursor=0 #내부적 인덱스에 사용
    self.on_screen_cursor=0 #외부적 인덱스에 사용

    self.pc_inventory=pc_inventory
    self.myFont=pygame.font.Font('Sejong hospital Light.ttf', 8)
    self.eventList=eventList
  def update(self, menuManager):
    
      for event in self.eventList:
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_DOWN:
            self.inner_cursor=self.inner_cursor+1 if self.inner_cursor+1<self.choice_count else self.choice_count-1
            self.on_screen_cursor=self.on_screen_cursor+1
          elif event.key == pygame.K_UP:
            self.inner_cursor=self.inner_cursor-1 if self.inner_cursor-1>0 else 0
            self.on_screen_cursor=self.on_screen_cursor-1
          elif event.key == pygame.K_e:
            self.sell()

      if self.on_screen_cursor>8:
        self.on_screen_cursor=8
        if self.show_end<self.choice_count:
          self.show_start+=1
          self.show_end+=1
      elif self.on_screen_cursor<0:
        self.on_screen_cursor=0
        if self.show_start>0:
          self.show_start-=1
          self.show_end-=1

  def sell(self):
    if self.pc_inventory.is_this_exist([self.menu_op_name[self.inner_cursor]]):
      self.pc_inventory.increase_money(self.pc_inventory.item_dic[self.menu_op_name[self.inner_cursor]].selling_price)
      self.pc_inventory.remove(self.menu_op_name[self.inner_cursor])
  def draw(self, screen):
    screen.fill((0, 0, 0)) #기존의 모든 요소 가리기
    screen.blit(menu_asset.menu_img, (0, 0))
    
    self.myText=self.myFont.render(str(self.pc_inventory.money), True, (255,255,255)) #myText 재할당 수정
    screen.blit(self.myText, (0, 0))
    
    idx=0
    for j in range(self.show_start, self.show_end):
      screen.blit(self.item_group_list[j].image,
          (vari.SCREEN_HEIGHT//10, vari.SCREEN_HEIGHT*(1/10)*(idx+1)))

      self.myText=self.myFont.render(self.item_group_list[j].name, True, (255,255,255))
      screen.blit(self.myText, (128, vari.SCREEN_HEIGHT*(1/10)*(idx+1)))

      self.myText=self.myFont.render(str(self.item_group_list[j].selling_price), True, (255,255,255))
      screen.blit(self.myText, (288, vari.SCREEN_HEIGHT*(1/10)*(idx+1)))

      idx+=1

    screen.blit(menu_asset.cursor_img, (vari.SCREEN_WIDTH*(1/10), vari.SCREEN_HEIGHT*(1/10)*(self.on_screen_cursor+1)))

    


    

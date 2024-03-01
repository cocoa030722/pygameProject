import pygame

import menu_folder.menu_shop as menu_shop
import menu_folder.menu_shop_buy as menu_shop_buy
import menu_folder.menu_shop_sell as menu_shop_sell
import menu_folder.menu_witch as menu_witch
import menu_folder.menu as menu
import menu_folder.menu_fairy as menu_fairy


class Menu_manager:
  def __init__(self, pc_inventory, eventList):
    self.menu_list={ #메뉴 객체들의 목록
      'Menu':menu.Menu(eventList),
      'Menu_shop':menu_shop.Menu_shop(eventList),
      'Menu_shop_buy':menu_shop_buy.Menu_shop_buy(eventList, pc_inventory),
      'Menu_shop_sell':menu_shop_sell.Menu_shop_sell(eventList, pc_inventory),
      'Menu_witch':menu_witch.Menu_witch(eventList),
      'Menu_fairy':menu_fairy.Menu_fairy(eventList),
    }
    self.cur_menu=self.menu_list['Menu']

  def change_menu(self, menu_code):
    self.cur_menu=self.menu_list[menu_code]

  def draw(self, screen):
    self.cur_menu.draw(screen)
    
  def update(self, menuManager):
    self.cur_menu.update(menuManager)

  def close(self):
    self.cur_menu.cursor=0 #현 메뉴의 커서 초기화

    self.cur_menu=self.menu_list['Menu']
    self.cur_menu.cursor=0 #메인 메뉴의 커서 초기화
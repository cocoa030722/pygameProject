import pygame

import ingame_menu.inventory_menu as inventory_menu
import ingame_menu.help_menu as help_menu


class Ingame_menu_manager: 
  def __init__(self, eventList, pc_inventory):
    self.inventoryMenu=inventory_menu.Ingame_menu(pc_inventory)
    self.menu_list={'Inventory_menu': self.inventoryMenu,
                   }
    self.cur_menu=self.menu_list['Inventory_menu']
    self.eventList=eventList
  def change_menu(self):
    print('change_menu(no actual function)')

  def draw(self, screen):
    self.cur_menu.draw(screen)

  def update(self, ingameMenuManager):
    self.cur_menu.update(self.eventList, ingameMenuManager)

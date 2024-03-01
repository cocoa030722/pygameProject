import pygame

import ingame_menu.empty as empty
import item.harvest.wheat_harvest as wheat_harvest
import item.harvest.berry_harvest as berry_harvest
import item.ore.ore_gold as ore_gold
import item.processed.wheat_flour as wheat_flour
import item.seafood.seafood_crucian as seafood_crucian
import item.seed_folder.wheat_seed as wheat_seed
import item.seed_folder.berry_seed as berry_seed
import item.tool.tool_hoe as tool_hoe
import item.tool.tool_sickel as tool_sickel
import item.tool.tool_pickaxe as tool_pickaxe
import item.tool.tool_fishing_rod as tool_fishing_rod

pygame.init()

class Inventory:
  def __init__(self):
    self.inventory={'empty' : {'item' : empty.Item(), 'count' : 0},
                    'wheat_seed' : {'item' : wheat_seed.Item(), 'count' : 10},
                    'wheat_harvest' : {'item' : wheat_harvest.Item(), 'count' : 0},
                    'wheat_flour' : {'item' : wheat_flour.Item(), 'count' : 0},
                    'berry_seed' : {'item' : berry_seed.Item(), 'count' : 0},
                    'berry_harvest' : {'item' : berry_harvest.Item(), 'count' : 0},
                    'gold' : {'item' : ore_gold.Item(), 'count' : 0},
                    'seafood_crucian' : {'item' : seafood_crucian.Item(), 'count' : 0},
                    'tool_hoe' : {'item' : tool_hoe.Item(), 'count' : 1},
                    'tool_sickel' : {'item' : tool_sickel.Item(), 'count' : 1},
                    'tool_pickaxe' : {'item' : tool_pickaxe.Item(), 'count' : 1},
                    'tool_fishing_rod' : {'item' : tool_fishing_rod.Item(), 'count' : 1},
                  }
    
    self.money=100
      
    self.picked_item=self.inventory['wheat_seed']['item']
    self.myFont=pygame.font.Font('Sejong hospital Light.ttf', 8)
    
  def add(self, item_name):
    self.inventory[item_name]['count']+=1
    
  def remove(self, item_name):
    if self.inventory[item_name]['count']>0:
      self.inventory[item_name]['count']-=1

  def select(self, item):
    self.picked_item=self.inventory[item]

  def is_this_exist(self, item_name):
    return self.inventory[item_name]['count']>0

  def have_more_money_than(self, price):
    return self.money>=price
    
  def increase_money(self, amount):
    self.money+=amount
  def decrease_money(self, amount):
    self.money-=amount
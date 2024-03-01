from os import error
import pygame
import random
from function_object.shipping_box import Shipping_box

import screen_state

pygame.init()

def plowing(self, map): #map의 자갈 타일과 충돌 -> 자갈 타일을 평지로 변경
  print("plowing")
  target_tile=pygame.sprite.spritecollide(self.front, map.include_tile, False) #대상 타일
  for i in target_tile:
    if 'gravel' in i.tile_type:
      map.include_tile.remove(i)
      new_tile=map.tile_pack['field_plain_tile'].Tile()
      new_tile.loc_define(self.front.x, self.front.y)
      map.include_tile.add(new_tile)

def sowing(self, map, seed, total_day):
  print('sowing')
  print("pc loc", self.front.x, self.front.y)
  target_tile=pygame.sprite.spritecollide(self.front, map.include_tile, False) #대상 타일
  for i in target_tile:
    if i.is_this_tile['sowing_able'] and self.inventory.is_this_exist(seed):
      crop_name=seed.split('_')[0]
      if map.cropManager.add(crop_name, self.front.x, self.front.y, total_day):
        self.inventory.inventory[seed]['count']-=1

def harvest(self, cropManager):
  print("harvesting")
  target_harvest=pygame.sprite.spritecollide(self.front, cropManager.crop_group, False)
  for i in cropManager.crop_group:
    print("i.harvest_able:", i.harvest_able)
    print("i.loc:", i.rect.x, i.rect.y)
  for i in target_harvest:
    print("target_harvest.harvest_able:", i.harvest_able)
    print("target_harvest.loc:", i.rect.x, i.rect.y)
    if i.harvest_able:
      harvest_name=str(i.name)+'_harvest'
      self.inventory.add(harvest_name)
      cropManager.kill(i)
      print(i.name, ":", self.inventory.item_count[harvest_name])

def interact_npc(self, map): #수정 필요
  
  print('interact_npc')
  screen_state.chat_window_called=False
  for i in map.include_npc:
    if pygame.sprite.collide_rect(self.front, i):
      screen_state.chat_window_called=True
      return i

def fishing(self, target_tile):
  print('fishing')
  if 'water' in target_tile.tile_type and random.random()>0.4:
    self.inventory.add('seafood_crucian')
    print('get seafood_crucian')

def mining(self, target_tile):
  print('mining')
  if 'mountain' in target_tile.tile_type and random.random()>0.4:
    self.inventory.add('gold')
    print('get gold')

def throwing(self, target_object):
  print('throwing')
  for i in target_object:
    print(i.name)
    if i.name=='shipping_box':
      i.item_group.add(self.inventory.picked_item)
      self.inventory.remove(self.inventory.picked_item.name)
      print('shipping')
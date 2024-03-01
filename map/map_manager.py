import pygame

import map.map_field_1 as map_field_1
import map.map_field_2 as map_field_2
import map.map_field_3 as map_field_3

import map.map_river_1 as map_river_1
import map.map_river_2 as map_river_2
import map.map_river_3 as map_river_3

import map.map_mountain_1 as map_mountain_1
import map.map_mountain_2 as map_mountain_2
import map.map_mountain_3 as map_mountain_3

import map.variable as vari

'''평지 맵:농사->수확->가공품(초반 컨텐츠)
강 맵:낚시/사금/잠수->랜덤하게 고급 상품(기본 장비 구매 후 중반 컨텐츠)
산 맵:광석 채굴->기계 제작 or 임산물 채집(체력,소모품,시간 소모 극심한 후반 컨텐츠)
'''
class Map_manager:
  def __init__(self, npc_dic, pc_inventory):

    self.map_dic={'map_field_1' : map_field_1.Map(pc_inventory),
          'map_river_1' : map_river_1.Map(pc_inventory),
          'map_mountain_1' : map_mountain_1.Map(pc_inventory),

          'map_field_2' : map_field_2.Map(pc_inventory),
          'map_river_2' : map_river_2.Map(pc_inventory),
          'map_mountain_2' : map_mountain_2.Map(pc_inventory),

          'map_field_3' : map_field_3.Map(pc_inventory),
          'map_river_3' : map_river_3.Map(pc_inventory),
          'map_mountain_3' : map_mountain_3.Map(pc_inventory)}
    self.cur_map=self.map_dic['map_river_2']
    
  def change_map(self, name):
    if name in self.map_dic:
      self.cur_map=self.map_dic[name]
  def draw(self, screen):
    self.cur_map.draw_map(screen)
  def update(self, dayManager, mapManager):
    self.cur_map.update(dayManager, mapManager)
    
  def map_change_down(self):
    self.change_map(self.cur_map.next_map_name[0])
  def map_change_left(self):
    self.change_map(self.cur_map.next_map_name[1])
  def map_change_up(self):
    self.change_map(self.cur_map.next_map_name[2])
  def map_change_right(self):
    self.change_map(self.cur_map.next_map_name[3])

  
  def map_screen_down(self, pc_rect_y):
    if pc_rect_y>vari.ON_SCREEN_MAP_HEIGHT//2 and self.cur_map.on_screen_y<self.cur_map.map_height-vari.ON_SCREEN_MAP_HEIGHT:
      self.cur_map.on_screen_y+=vari.BLOCK
      
  def map_screen_left(self, pc_rect_x):
    if pc_rect_x<vari.ON_SCREEN_MAP_WIDTH//2 and self.cur_map.on_screen_x>=vari.BLOCK:
      self.cur_map.on_screen_x-=vari.BLOCK
    
  def map_screen_up(self, pc_rect_y):
    if pc_rect_y<vari.ON_SCREEN_MAP_HEIGHT//2 and self.cur_map.on_screen_y>=vari.BLOCK:
      self.cur_map.on_screen_y-=vari.BLOCK
      
  def map_screen_right(self, pc_rect_x):
    if pc_rect_x>vari.ON_SCREEN_MAP_WIDTH//2 and self.cur_map.on_screen_x<self.cur_map.map_width-vari.ON_SCREEN_MAP_WIDTH:
      self.cur_map.on_screen_x+=vari.BLOCK

  
  def new_screen_down(self, pc_x, pc_y):
    if pc_x-vari.ON_SCREEN_MAP_WIDTH//2<0:
      self.cur_map.on_screen_x=0
    elif pc_x-vari.ON_SCREEN_MAP_WIDTH//2>self.cur_map.map_width-vari.ON_SCREEN_MAP_WIDTH:
      self.cur_map.on_screen_x=self.cur_map.map_width-vari.ON_SCREEN_MAP_WIDTH
    else:
      self.cur_map.on_screen_x=pc_x-vari.ON_SCREEN_MAP_WIDTH//2
    self.cur_map.on_screen_y=0
    
  def new_screen_left(self, pc_x, pc_y):
    self.cur_map.on_screen_x=(self.cur_map.map_width-vari.ON_SCREEN_MAP_WIDTH)
    if pc_y-vari.ON_SCREEN_MAP_HEIGHT//2<0:
      self.cur_map.on_screen_y=0
    elif pc_y-vari.ON_SCREEN_MAP_HEIGHT//2>self.cur_map.map_height-vari.ON_SCREEN_MAP_HEIGHT:
      self.cur_map.on_screen_y=self.cur_map.map_height-vari.ON_SCREEN_MAP_HEIGHT
    else:
      self.cur_map.on_screen_y=pc_y-vari.ON_SCREEN_MAP_HEIGHT//2
      
  def new_screen_up(self, pc_x, pc_y):
    if pc_x-vari.ON_SCREEN_MAP_WIDTH//2<0:
      self.cur_map.on_screen_x=0
    elif pc_x-vari.ON_SCREEN_MAP_WIDTH//2>self.cur_map.map_width-vari.ON_SCREEN_MAP_WIDTH:
      self.cur_map.on_screen_x=self.cur_map.map_width-vari.ON_SCREEN_MAP_WIDTH
    else:
      self.cur_map.on_screen_x=pc_x-vari.ON_SCREEN_MAP_WIDTH//2
    self.cur_map.on_screen_y=(self.cur_map.map_height-vari.ON_SCREEN_MAP_HEIGHT)
    
  def new_screen_right(self, pc_x, pc_y):
    self.cur_map.on_screen_x=0

    if pc_y-vari.ON_SCREEN_MAP_HEIGHT//2<0:
      self.cur_map.on_screen_y=0
    elif pc_y-vari.ON_SCREEN_MAP_HEIGHT//2>self.cur_map.map_height-vari.ON_SCREEN_MAP_HEIGHT:
      self.cur_map.on_screen_y=self.cur_map.map_height-vari.ON_SCREEN_MAP_HEIGHT
    else:
      self.cur_map.on_screen_y=pc_y-vari.ON_SCREEN_MAP_HEIGHT//2



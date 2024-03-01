import pygame

import map.variable as vari

pygame.init()

def move_up(self):
  if self.front.pre_dir==self.front.dir:
     self.y -= vari.BLOCK
def move_down(self):
  if self.front.pre_dir==self.front.dir:
    self.y += vari.BLOCK
def move_left(self):
  if self.front.pre_dir==self.front.dir:
    self.x -= vari.BLOCK
def move_right(self):
  if self.front.pre_dir==self.front.dir:
    self.x += vari.BLOCK

def move_dir_up(self):
  self.front.pre_dir=self.front.dir
  self.front.dir=2
def move_dir_down(self):
  self.front.pre_dir=self.front.dir
  self.front.dir=0
def move_dir_left(self):
  self.front.pre_dir=self.front.dir
  self.front.dir=1
def move_dir_right(self):
  self.front.pre_dir=self.front.dir
  self.front.dir=3

def map_change(self, mapManager):
  is_changed_dir=[False, False, False, False]
  if self.front.y>=mapManager.cur_map.map_height:
    mapManager.map_change_down()
    is_changed_dir[0]=True
  elif self.front.x<0:
    mapManager.map_change_left()
    is_changed_dir[1]=True
  elif self.front.y<0:
    mapManager.map_change_up()
    is_changed_dir[2]=True
  elif self.front.x>=mapManager.cur_map.map_width:
    mapManager.map_change_right()
    is_changed_dir[3]=True
  return is_changed_dir

def move_another_map_check(self, mapManager):
  port=map_change(self, mapManager)
  if port[0]:
    print('down')
    self.x=self.x
    self.y=0
    self.front.update(self.x, self.y, mapManager.cur_map)
    mapManager.new_screen_down(self.x, self.y)
    
  elif port[1]:
    print('left')
    self.x=(mapManager.cur_map.map_width-vari.BLOCK)
    self.y=self.y
    self.front.update(self.x, self.y, mapManager.cur_map)
    mapManager.new_screen_left(self.x, self.y)
    
  elif port[2]:
    print('up')
    self.x=self.x
    self.y=(mapManager.cur_map.map_height-vari.BLOCK)
    self.front.update(self.x, self.y, mapManager.cur_map)
    mapManager.new_screen_up(self.x, self.y)
    
  elif port[3]:
    print('right')
    self.x=0
    self.y=self.y
    self.front.update(self.x, self.y, mapManager.cur_map)
    mapManager.new_screen_right(self.x, self.y)

def move_through_door(self, door, mapManager):
  mapManager.change_map(door.destination)
  self.x=0
  self.y=0
  self.front.update(self.x, self.y, mapManager.cur_map)
  #mapManager.new_screen(self.x, self.y)
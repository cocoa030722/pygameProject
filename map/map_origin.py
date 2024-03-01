import pygame

import crop_folder.crop_manager as crop_manager
import map.map_draw as map_draw
import map.variable as vari
import npc.npc_manager as npc_manager

pygame.init()


class Map_origin: #띄어쓰기 조심
  '''
  def __init__(self):
    self.next_map_name=['map_field_2', 'invalid_map', 'invalid_map', 'map_river_1']
    self.name='map_field_1'
    
    self.cropManager=crop_manager.Crop_manager()
    self.include_npc=pygame.sprite.Group()
    self.include_building=pygame.sprite.Group()
    self.include_field_item=pygame.sprite.Group()
    self.include_tile=pygame.sprite.Group()
    self.include_object=pygame.sprite.Group()
    
    self.tile_pack=[]
    #전체 맵의 크기
    self.map_width=(vari.SCREEN_WIDTH)*2
    self.map_height=(vari.SCREEN_HEIGHT//10*9)*2

    #화면의 좌표
    self.on_screen_x=0
    self.on_screen_y=0

    def draw_map(self, screen):
      map_draw.map_draw(self, screen)
        
    def update(self, dayManager, mapManager):
      print("map update")
      self.include_npc.update()
      self.include_object.update(dayManager, mapManager)
      self.cropManager.update(dayManager, mapManager)
  '''

  def __init__(self):
    self.next_map_name=['map_field_2', 'invalid_map', 'invalid_map', 'map_river_1']
    self.name='map_field_1'

    self.cropManager=crop_manager.Crop_manager()
    self.npcManager=npc_manager.Npc_manager()
    self.include_building=[]
    self.include_field_item=pygame.sprite.Group()
    self.include_tile=pygame.sprite.Group()
    self.include_object=pygame.sprite.Group()

    self.tile_pack=[]
    #전체 맵의 크기
    self.map_width=(vari.SCREEN_WIDTH)*2
    self.map_height=(vari.SCREEN_HEIGHT//10*9)*2

    #화면의 좌표
    self.on_screen_x=0
    self.on_screen_y=0

  def draw_map(self, screen):
    map_draw.map_draw(self, screen)

  def update(self, dayManager, mapManager):
    self.include_tile.update(mapManager)
    self.npcManager.update(mapManager)
    self.include_object.update(dayManager, mapManager)
    for i in self.include_building:
      i.update(mapManager)
    self.cropManager.update(dayManager, mapManager)
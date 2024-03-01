import pygame

import map.variable as vari
import pc.inventory as inventory
import pc.pc_front as front
import pc.action as action
import pc.move as move
import pc.asset as asset

class Pc(pygame.sprite.Sprite):
  def __init__(self, eventList):
    pygame.sprite.Sprite.__init__(self)
    #전체 맵 상에서의 좌표
    self.x = 0
    self.y = 0
    
    self.image=asset.player_img
    self.image=pygame.transform.scale(self.image, (vari.BLOCK,vari.BLOCK))
    self.rect=self.image.get_rect()
    self.rect.x=self.x
    self.rect.y=self.y
    self.npc='ailce'
    self.ownership=['map_river_2'] #자신 소유 부지에서만 생산 가능하도록 하는 리스트
    self.front=front.PlayerFront()
    self.inventory=inventory.Inventory()
    self.eventList=eventList
    
  def draw(self, screen):
    screen.blit(self.image, (self.rect.x, self.rect.y))
    self.front.draw(screen)
      
  def update(self, mapManager, ingameMenuManager, dayManager):
    out_of_bound = (0>self.front.x or self.front.x>=mapManager.cur_map.map_width or 0>self.front.y or self.front.y>=mapManager.cur_map.map_height)
    
    target_door=[]
    for i in mapManager.cur_map.include_building:
      target_door.append(pygame.sprite.spritecollide(self.front, i.include_door, False))
      
    target_tile=pygame.sprite.spritecollide(self.front, mapManager.cur_map.include_tile, False)
    target_object=pygame.sprite.spritecollide(self.front, mapManager.cur_map.include_object, False)
    target_field_item=pygame.sprite.spritecollide(self.front, mapManager.cur_map.include_field_item, False)

    forward_able=(len(target_tile)<=0 or target_tile[0].is_this_tile['pass_able']) and (len(target_field_item)<=0)
    
    for event in self.eventList:
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
          move.move_dir_up(self)
          if out_of_bound:
            move.move_another_map_check(self, mapManager)
          elif forward_able:
            move.move_up(self)
            mapManager.map_screen_up(self.rect.y)
          
        elif event.key == pygame.K_DOWN:
          move.move_dir_down(self)
          if out_of_bound:
            move.move_another_map_check(self, mapManager)
          elif forward_able:
            move.move_down(self)
            mapManager.map_screen_down(self.rect.y)
            
        elif event.key == pygame.K_RIGHT:
          move.move_dir_right(self)
          if out_of_bound:
            move.move_another_map_check(self, mapManager)
          elif forward_able:
            move.move_right(self)
            mapManager.map_screen_right(self.rect.x)
            
        elif event.key == pygame.K_LEFT:
          move.move_dir_left(self)
          if out_of_bound:
            move.move_another_map_check(self, mapManager)
          elif forward_able:
            move.move_left(self)
            mapManager.map_screen_left(self.rect.x)
              
        elif event.key == pygame.K_f: #인게임 정보(도움말, 퀘스트 진척도)
          print("info")
          
        elif event.key == pygame.K_r: #npc 대화 버튼
          print('interact_npc')
          self.npc=action.interact_npc(self, mapManager.cur_map)

        elif event.key == pygame.K_c: #아이템 버리기 버튼
          print(len(target_tile), len(target_object))
          action.throwing(self, target_object)
        elif event.key == pygame.K_e: #상호작용 버튼
          print('interact_tool')
          item_name=ingameMenuManager.cur_menu.picked_item.name.split('_')
          print(len(item_name), item_name)
          
          if len(target_door)>0 and len(target_door[0])>0:
            move.move_through_door(self, target_door[0][0], mapManager)
            
          if (mapManager.cur_map.name not in self.ownership):
            print('not in ownership')
            
          if len(item_name)>=1 and item_name[0]=='tool':
            if ingameMenuManager.cur_menu.picked_item.plow_able and (mapManager.cur_map.name in self.ownership):
              action.plowing(self, mapManager.cur_map)
            
            elif ingameMenuManager.cur_menu.picked_item.harvest_able and (mapManager.cur_map.name in self.ownership):
              action.harvest(self, mapManager.cur_map.cropManager)

            elif ingameMenuManager.cur_menu.picked_item.fishing_able and (mapManager.cur_map.name in self.ownership):
              action.fishing(self, target_tile[0])

            elif ingameMenuManager.cur_menu.picked_item.mining_able and (mapManager.cur_map.name in self.ownership):
              action.mining(self, target_tile[0])
              
          elif len(item_name)>=2 and item_name[1]=='seed':
            if (mapManager.cur_map.name in self.ownership):
              action.sowing(self, mapManager.cur_map, ingameMenuManager.cur_menu.picked_item.name, dayManager.total_day)
              print('sowing')
              
          

    self.front.update(self.x, self.y, mapManager.cur_map)
    self.inventory.select(ingameMenuManager.cur_menu.picked_item)

    self.rect.x=self.x-mapManager.cur_map.on_screen_x if self.x-mapManager.cur_map.on_screen_x>0 else self.x
    self.rect.y=self.y-mapManager.cur_map.on_screen_y if self.y-mapManager.cur_map.on_screen_y>0 else self.y

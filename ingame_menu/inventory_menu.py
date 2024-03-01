import pygame

import ingame_menu.ingame_menu_asset as ingame_menu_asset
import ingame_menu.action as action
import ingame_menu.ingame_menu_tile as ingame_menu_tile
import map.variable as vari

pygame.init()

class Ingame_menu(pygame.sprite.Sprite):
  def __init__(self, pc_inventory):
    pygame.sprite.Sprite.__init__(self)
    self.menu_name='Inventory_menu'
    self.choice_count=9

    self.myFont=pygame.font.Font('Sejong hospital Light.ttf', 8)
      
    self.is_clicked=False
    self.cursor=-1
    self.cursor_img_rect=ingame_menu_asset.cursor_img.get_rect()
    self.cursor_img_rect.left=1000
    self.cursor_img_rect.top=1000

    self.rect=ingame_menu_asset.inventory_menu_rect
    self.menu_tile_list=[]
    self.item_group=pygame.sprite.Group()
    
    for i in range(0, self.choice_count):
      self.menu_tile_list.append(ingame_menu_tile.Tile(i, ((vari.SCREEN_WIDTH//9)*i), ingame_menu_asset.inventory_menu_rect.y))

    idx=0
    for i in pc_inventory.inventory:
      if idx<self.choice_count and pc_inventory.is_this_exist(i):
        print(i)
        self.menu_tile_list[idx].include_item=i
        self.item_group.add(pc_inventory.inventory[i]['item'])
        idx+=1

    self.pc_inventory=pc_inventory
    
    self.picked_item=self.menu_tile_list[0].include_item

    self.picked_item_info='pick item: '+str(self.picked_item)
    self.picked_item_info_text=self.myFont.render(self.picked_item_info, True, (0,0,0))

    self.picked_item_info_rect=self.picked_item_info_text.get_rect()
    self.picked_item_info_rect.x=ingame_menu_asset.inventory_menu_rect.x+64
    self.picked_item_info_rect.y=ingame_menu_asset.inventory_menu_rect.y+vari.SCREEN_WIDTH//9
    
  def update(self, eventList, ingameMenuManager):

    for event in eventList:
      if event.type == pygame.MOUSEBUTTONDOWN:
        if self.rect.collidepoint(event.pos):
          self.is_clicked=True
          print("메뉴 클릭됨")
          for i in self.menu_tile_list:
            if i.rect.collidepoint(event.pos):
              
              action.item_move(self.cursor, i, self.menu_tile_list[self.cursor])
              if action.is_tile_doublepick(i, self.menu_tile_list[self.cursor]):
                self.cursor=-1
              else:
                self.cursor=i.order
              print(self.cursor)
        else:
          self.is_clicked=False
          print("메뉴 클릭되지 않음")
          self.cursor=-1
          
    self.cursor_img_rect.left=self.menu_tile_list[self.cursor].rect.x+24
    self.cursor_img_rect.top=self.menu_tile_list[self.cursor].rect.y
    
        
    for i in self.pc_inventory.inventory:
      if (self.pc_inventory.inventory[i]['item'] not in self.item_group) and self.pc_inventory.is_this_exist(i):
        print('before:', self.item_group)
        self.item_group.add(i)
        print('after:', self.item_group)
        print(i)
        for j in self.menu_tile_list:
          if j.include_item.name=='empty':
            j.add(i, self.pc_inventory)
            break
            
    for i in range(len(self.menu_tile_list)):
      self.menu_tile_list[i].update(self.menu_tile_list[i].include_item, self.pc_inventory)
      if self.menu_tile_list[i].include_item_count==0:
        self.item_group.remove(self.menu_tile_list[i].include_item)
        self.menu_tile_list[i].remove()


    self.picked_item_info='pick item: '+str(self.picked_item)
    self.picked_item_info_text=self.myFont.render(self.picked_item_info, True, (0,0,0))
    
    if self.cursor!=-1:
      self.picked_item=self.menu_tile_list[self.cursor].include_item
      
  def draw(self, screen):
    screen.fill((204, 204, 204), ingame_menu_asset.inventory_menu_rect)
    
    screen.blit(self.picked_item_info_text, (self.picked_item_info_rect.x, self.picked_item_info_rect.y))
    
    for i in range(self.choice_count):
      
      screen.blit(self.menu_tile_list[i].image, (self.menu_tile_list[i].rect.x, self.menu_tile_list[i].rect.y))
      if i==self.cursor:
        screen.fill((255, 255, 102), self.cursor_img_rect)
      
      screen.blit(self.menu_tile_list[i].include_item.image, (self.menu_tile_list[i].rect.x+4, self.menu_tile_list[i].rect.y+4))
      include_item_count=self.myFont.render(str(self.menu_tile_list[i].include_item_count), True, (0,0,0))
      screen.blit(include_item_count, (self.menu_tile_list[i].rect.x+16, self.menu_tile_list[i].rect.y+16))
    



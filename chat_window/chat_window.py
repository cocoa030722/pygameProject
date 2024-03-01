import pygame

import map.variable as vari

pygame.init()

class Chat_window(pygame.sprite.Sprite):
  def __init__(self, eventList):
    self.rect=pygame.Rect((0, (vari.SCREEN_HEIGHT//3)*2), (vari.SCREEN_WIDTH, vari.SCREEN_HEIGHT//3))
    self.myFont=pygame.font.Font('Sejong hospital Light.ttf', 12)
    self.choice_count=3
    self.cursor_raw=pygame.image.load('core/src/main/assets/interfaces/icons.png')

    self.cursor_img=pygame.Surface.subsurface(self.cursor_raw, (16,16,16,16))
    self.cursor=0
    self.cursor_img_rect=self.cursor_img.get_rect()
    self.cursor_img_rect.x=self.rect.x
    self.cursor_img_rect.y=(self.rect.y)+(16)*self.cursor
    
    self.choice_list=[]
    self.item_group=pygame.sprite.Group()

    for i in range(0, self.choice_count):
      self.choice_list.append('placeholder')
    self.eventList=eventList
    
  def update(self, mapManager, pc_object):
    for event in self.eventList:
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
          self.cursor=self.cursor+1 if self.cursor+1<self.choice_count else self.choice_count-1
        elif event.key == pygame.K_UP:
          self.cursor=self.cursor-1 if self.cursor-1>0 else 0
        elif event.key == pygame.K_r:
          pc_object.npc.choice_list[self.cursor].act(mapManager.cur_map, pc_object.npc, pc_object)
        
    self.cursor_img_rect.top=self.rect.y+(24)*self.cursor
  def draw(self, screen, npc):
    screen.fill((150, 150, 150), self.rect)
    screen.blit(self.cursor_img, (self.cursor_img_rect.left, self.cursor_img_rect.top))
    
    #npc 스탠딩 불러오기
    #npc_img=pygame.transform.scale(npc_sprite.standing, (48, 48))
    #screen.blit(npc_img, (vari.screen_width-48, ((vari.screen_height/3)*2)-48))

    str_name=self.myFont.render(npc.name, True, (255,255,255))
    screen.blit(str_name, (4, self.rect.y-16))

    str_reputation=self.myFont.render(str(npc.reputation), True, (255,255,255))
    screen.blit(str_reputation, (44, self.rect.y-16))
    
    idx=0
    for i in npc.choice_list:
      myText=self.myFont.render(i.name, True, (255,255,255))
      screen.blit(myText, (24, self.rect.y+(idx*24)))
      idx+=1


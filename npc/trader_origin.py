import pygame

import npc.action.attack as act_attack
import npc.action.blame as act_blame
import npc.action.praise as act_praise
import npc.npc_tile as npc_tile
import npc.npc_origin as npc_origin
import map.variable as vari

pygame.init()

class Trader(npc_origin.Npc_origin):
  def __init__(self, x, y):
      super().__init__(x, y)
      self.x = x
      self.y = y
      self.image=npc_tile.npc_ailce
      self.image=pygame.transform.scale(self.image, (vari.BLOCK,vari.BLOCK))
      self.standing=npc_tile.ailce_standing
      self.rect=self.image.get_rect()
      self.rect.left=self.x
      self.rect.top=self.y
      self.name='tool_trader'
      self.reputation=0
      self.choice_list=[act_praise, act_blame, act_attack]
    
      self.items = pygame.sprite.Group()
      
  def buy_item(self, item):
    if item in self.items:
      return f"{item} is already in stock."
    self.items.add(item)
    return f"{item} added to stock."
        
  def sell_item(self, item):
    if item not in self.items:
      return f"{item} is not available for sale."
    self.items.add(item)
    return f"{item} sold."
      
  def update(self):
    self.rect.left=self.x
    self.rect.top=self.y
    
  def draw(self, screen):
    screen.blit(self.image, (self.rect.x, self.rect.y))

import pygame

pygame.init()

class Ingame_info(pygame.sprite.Sprite):
  def __init__(self, pc_inventory):
    pygame.sprite.Sprite.__init__(self)
    self.myFont=pygame.font.Font('Sejong hospital Light.ttf', 8)
    
    self.money_info='돈: '+str(pc_inventory.money)
    self.money_info_text=self.myFont.render(self.money_info, True, (0,0,0))

    self.money_info_rect=self.money_info_text.get_rect()
    self.money_info_rect.x=0
    self.money_info_rect.y=0
    self.pc_inventory=pc_inventory
  def update(self):
    self.money_info='돈: '+str(self.pc_inventory.money)
    self.money_info_text=self.myFont.render(self.money_info, True, (255,0,0))
  
  def draw(self, screen):
    screen.blit(self.money_info_text, (self.money_info_rect.x, self.money_info_rect.y))
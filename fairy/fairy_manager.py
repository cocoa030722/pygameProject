import pygame

import fairy.harvest.harvest_1 as harvest_1
pygame.init()

class Fairy_manager:
  def __init__(self):

    self.fairy_dic={'harvest_1' : harvest_1.Fairy(),
                 }
    
    self.harvest_team=pygame.sprite.Group()
    for i in self.fairy_dic:
      if i.split('_')[0]=='harvest':
        self.harvest_team.add(self.fairy_dic[i])
    

  def draw(self, screen):
    self.harvest_team.draw(screen)

  def update(self):
    self.harvest_team.update()
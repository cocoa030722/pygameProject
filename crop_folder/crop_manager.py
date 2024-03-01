import pygame

import crop_folder.crop_wheat as crop_wheat
import crop_folder.crop_berry as crop_berry

pygame.init()


crop_dic={'wheat' : crop_wheat, 
          'berry' : crop_berry, 
         }

class Crop_manager:
  def __init__(self):
    self.crop_group=pygame.sprite.Group()
    
  def add(self, crop_name, x, y, total_day): #작물 추가의 성공 여부를 bool로 리턴
    add_success=False
    already_exist=False
    for i in self.crop_group:
      if i.x==x and i.y==y:
        already_exist=True
        break

    if not already_exist:
      self.crop_group.add(crop_dic[crop_name].Crop(x, y, total_day))
      print("new crop loc:", self.crop_group.sprites()[len(self.crop_group.sprites())-1].x, self.crop_group.sprites()[len(self.crop_group.sprites())-1].y)
      add_success=True
    return add_success
    
    
  def kill(self, crop):
    self.crop_group.remove(crop)
    print('crop_manager:crop kill')
        
  def draw(self, screen):
    self.crop_group.draw(screen)

  def update(self, dayManager, mapManager):
    for i in self.crop_group:
      i.update(dayManager, mapManager)
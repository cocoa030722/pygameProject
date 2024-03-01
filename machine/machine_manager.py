import pygame

import machine.machine_mill as machine_mill

pygame.init()

machine_dic={'mill' : machine_mill,
         }


class Machine_manager:
  def __init__(self):
    self.machine_group=pygame.sprite.Group()
    
  def add(self, machine_name, x, y, pc_inventory): #기계 추가의 성공 여부를 bool로 리턴
    add_success=False
    already_exist=False
    for i in self.machine_group:
      print(i.rect.x, i.rect.y)
      if i.rect.x==x and i.rect.y==y:
        already_exist=True
        break

    if not already_exist:
      self.machine_group.add(machine_dic[machine_name].Machine(x, y))
      self.machine_group.sprites()[len(self.machine_group.sprites())-1].rect.x=x
      self.machine_group.sprites()[len(self.machine_group.sprites())-1].rect.y=y
      add_success=True
    return add_success
    
    
  def kill(self, crop):
    self.machine_group.remove(crop)
    print('kill')
        
  def draw(self, screen):
    self.machine_group.draw(screen)

  def update(self):
    self.machine_group.update()
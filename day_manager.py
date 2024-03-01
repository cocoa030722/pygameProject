import pygame

pygame.init()


class Day_manager:
  def __init__(self):
    self.start_time=pygame.time.get_ticks()
    self.cur_time=pygame.time.get_ticks()
    self.passed_time=self.cur_time-self.start_time
    self.total_day=0
    self.day=self.total_day%30
    self.month=(self.total_day//30)%4
    self.year=self.total_day//120
    self.myFont=pygame.font.Font('Sejong hospital Light.ttf', 8)
  def update(self):
    self.cur_time=pygame.time.get_ticks()
    self.passed_time=self.cur_time-self.start_time
    if self.passed_time>=10*1000: #10*1000ms=10초
      self.passed_time=0
      self.start_time=pygame.time.get_ticks()
      
      self.total_day+=1
      self.day=self.total_day%30
      self.month=(self.total_day//30)%4
      self.year=self.total_day//120

  def draw(self, screen):
    myText=self.myFont.render('day: '+str(self.day), True, (255,255,255))
    screen.blit(myText, (0, 0))
    myText=self.myFont.render('month: '+str(self.month), True, (255,255,255))
    screen.blit(myText, (0, 24))
    myText=self.myFont.render('year: '+str(self.year), True, (255,255,255))
    screen.blit(myText, (0, 44))
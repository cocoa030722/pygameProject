import pygame

pygame.init()
#도전과제/퀘스트 관련 구현
class Achievement:
  
    def __init__(self):
        self.harvest_count = 0
        self.sell_count = 0

    def track_harvest(self):
        self.harvest_count += 1
        if self.harvest_count >= 1000:
            self.record_achievement("Harvest Challenge Completed!")

    def track_sell(self):
        self.sell_count += 1
        if self.sell_count >= 1000:
            self.record_achievement("Sell Challenge Completed!")

    def record_achievement(self, message):
        # Record achievement logic here
        print(message)
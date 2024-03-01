import pygame

import day_manager
import display
import game_update
import ingame_info
import fairy.fairy_manager as fairy_manager
import map.map_manager as map_manager
import npc.npc_manager as npc_manager
import menu_folder.menu_manager as menu_manager
import ingame_menu.ingame_menu_manager as ingame_menu_manager
import chat_window.chat_window as chat_window
import pc.pc as pc
import screen_state

pygame.init()

pygame.display.set_caption("PyGame")
running = True  #게임 진행 여부에 대한 변수 True : 게임 진행 중
clock = pygame.time.Clock()


eventList = [] #이벤트를 복사해서 전달하는 리스트
pc_object=pc.Pc(eventList)
#매니저 객체들:각 집합의 모든 요소를 선언한 후 저장/관리
essential_pack={'menuManager':menu_manager.Menu_manager(pc_object.inventory, eventList),
              'ingameMenuManager':ingame_menu_manager.Ingame_menu_manager(eventList, pc_object.inventory),
              'mapManager':map_manager.Map_manager(npc_manager.npc_dic, pc_object.inventory),
              #'fairyManager':fairy_manager.Fairy_manager(),
              'dayManager':day_manager.Day_manager(),
              'ingame_info_object':ingame_info.Ingame_info(pc_object.inventory),
              'chatWindow':chat_window.Chat_window(eventList)
}


while running:
  eventList.clear() #리스트 초기화
  for event in pygame.event.get():
    eventList.append(event)
    if event.type == pygame.QUIT:  #창을 닫는 이벤트 발생했는가?
      running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_m:
        screen_state.menu_called = not screen_state.menu_called

      elif event.key == pygame.K_0: #팝업 강제종료
        screen_state.menu_called = False
        screen_state.chat_window_called = False
  game_update.update(essential_pack, pc_object)
  display.draw(essential_pack, pc_object)
  pygame.display.update()
  clock.tick(30)

#pygame 종료
pygame.quit()

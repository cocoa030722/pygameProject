import pygame


pygame.init()

#alice, chris, gosegu, ina, laplus
npc_raw1=pygame.image.load('core/src/main/assets/sprites/avatars.png')
npc_ailce=pygame.Surface.subsurface(npc_raw1, (0,0,24,30))
npc_chris=pygame.Surface.subsurface(npc_raw1, (24,0,24,30))
npc_gosegu=pygame.Surface.subsurface(npc_raw1, (48,0,24,30))
npc_ina=pygame.Surface.subsurface(npc_raw1, (72,0,24,30))
npc_laplus=pygame.Surface.subsurface(npc_raw1, (96,0,24,30))
#miko, pekora
npc_raw2=pygame.image.load('core/src/main/assets/sprites/brute.png')
npc_miko=pygame.Surface.subsurface(npc_raw2, (0,0,12,16))
npc_pekora=pygame.Surface.subsurface(npc_raw2, (0,16,12,16))
#suisei
npc_raw3=pygame.image.load('core/src/main/assets/sprites/ratking.png')
npc_suisei=pygame.Surface.subsurface(npc_raw3, (0,0,14,18))

ailce_standing=pygame.image.load('npc_standing/ailce.jpg')
chris_standing=pygame.image.load('npc_standing/chris.jpg')
gosegu_standing=pygame.image.load('npc_standing/gosegu.jpg')
ina_standing=pygame.image.load('npc_standing/ina.jpg')
laplus_standing=pygame.image.load('npc_standing/laplus.jpg')
miko_standing=pygame.image.load('npc_standing/miko.jpg')
pekora_standing=pygame.image.load('npc_standing/pekora.jpg')
suisei_standing=pygame.image.load('npc_standing/suisei.jpg')

import pygame

pygame.init()


def item_move(cursor, picked_tile, pre_tile):
  print("item_move", picked_tile.order, pre_tile.order)
  if cursor!=-1:
    
    temp=picked_tile.include_item
    picked_tile.include_item=pre_tile.include_item
    pre_tile.include_item=temp
      
def is_tile_doublepick(picked_tile, pre_tile):
  print("tile_pick on", picked_tile.order)
  if picked_tile.order==pre_tile.order:
    print("tile_pick off")
  return picked_tile.order==pre_tile.order
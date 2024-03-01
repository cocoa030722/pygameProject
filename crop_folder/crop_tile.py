import pygame

import item.seed_folder.seed_asset as seed_asset
import item.harvest.harvest_asset as harvest_asset

pygame.init()

farm1=pygame.image.load('core/src/main/assets/environment/terrain_features.png')

wheat_seed_image=seed_asset.wheat_seed_image
#wheat_grow_n_image=pygame.Surface.subsurface(farm1, (10*16,0,16,16))
wheat_harvest_image=harvest_asset.wheat_harvest_image

berry_seed_image=seed_asset.berry_seed_image
berry_harvest_image=harvest_asset.berry_harvest_image


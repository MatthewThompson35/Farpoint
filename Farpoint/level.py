import pygame
from settings import *
from tile import *
from player import *
from debug import debug

class Level:
    def __init__(self):
        
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        
        self.create_map()
        
        
    def create_map(self):
        for row_index,row in enumerate(WORLD_MAP):
            for col_index,tile in enumerate(row):
                pos = (col_index * TILESIZE, row_index * TILESIZE)
                if tile == 'x':
                    Tile(pos,self.visible_sprites)
                elif tile == 'p':
                    self.player = Player(pos,self.visible_sprites)
                    
        
        
        
    def run(self):
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
        debug(self.player.direction)
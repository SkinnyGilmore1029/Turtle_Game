import pygame
from Utility.Settings import WIDTH,HEIGHT
from .Background_manger import Level_Backgrounds

class Level_Creater:
    def __init__(self,level:int,room:int):
        self.background = Level_Backgrounds(level,room)
        
    def draw_level(self,screen):
        self.background.draw(screen)
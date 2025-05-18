import pygame
from Utility.Settings import WIDTH,HEIGHT
from .Background_manger import Level_Backgrounds
from The_turtles.The_player import player
from The_turtles.Jesse import jesse
from .The_Enemies import test_monster

class Level_Creater:
    def __init__(self,level:int,room:int):
        self.backgrounds:dict[tuple,Level_Backgrounds] = {}
        self.level = level
        self.room = room
        self.background = Level_Backgrounds(level,room)
    
    def get_background(self,level:int,room:int):
        key = (level, room)
        if key not in self.backgrounds:
            self.backgrounds[key] = Level_Backgrounds(level,room)
        return self.backgrounds[key]
    
    def change_background(self,new_level:int,new_room:int)->None:
        self.level = new_level
        self.room = new_room
        self.background = self.get_background(new_level, new_room)
    
    def update_level(self,dt:float)->None:
        player.update(dt)
        test_monster.update(dt)
    
    def draw_level(self,screen:pygame.Surface)->None:
        self.background.draw(screen)
        player.draw(screen)
        test_monster.draw(screen)
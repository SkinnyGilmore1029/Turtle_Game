import pygame
from .Background_manger import Level_Backgrounds
from .Wall_manger import All_walls
from .Collectables_Group import Collect_group
from The_turtles.The_player import player
from Enemy.The_Enemy_Group import bad_guys


class Level_Creater:
    def __init__(self,level:int,room:int):
        self.backgrounds:dict[tuple,Level_Backgrounds] = {}
        self.level = level
        self.room = room
        self.background = Level_Backgrounds(level,room)
        bad_guys.get_level_badguys(level,room)
        All_walls.load_group(level,room)
        Collect_group.get_level_keys(level,room)
    
    def get_background(self,level:int,room:int):
        key = (level, room)
        if key not in self.backgrounds:
            self.backgrounds[key] = Level_Backgrounds(level,room)
        return self.backgrounds[key]
    
    def change_background(self,new_level:int,new_room:int)->None:
        self.level = new_level
        self.room = new_room
        self.background = self.get_background(new_level, new_room)
    
    def change_badguys(self,new_level:int,new_room:int)->None:
        self.level = new_level
        self.room = new_room
        bad_guys.get_level_badguys(new_level,new_room)
    
    def change_walls(self,new_level:int,new_room:int)->None:
        self.level = new_level
        self.room = new_room
        All_walls.change_level()
        All_walls.load_group(new_level,new_room)
    
    def change_rooms(self,new_level:int,new_room:int)->None:
        self.change_background(new_level,new_room)
        self.change_badguys(new_level,new_room)
        self.change_walls(new_level,new_room)
    
    def handle_collision(self):
        if bad_guys.collision_with_player(player):
            player.died()
        #Collect_group.collision_with_player(player)
    
    def update_level(self,dt:float)->None:
        player.update(dt)
        bad_guys.update(dt)
        Collect_group.update(player)
    
    def draw_level(self,screen:pygame.Surface)->None:
        self.background.draw(screen)
        All_walls.draw(screen,player)
        player.draw(screen)
        bad_guys.draw(screen)
        Collect_group.draw(screen)
        
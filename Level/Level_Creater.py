import pygame
from .Background_manger import Level_Backgrounds
from .Wall_manger import All_walls
from .Collectables_Group import Collect_group
from .Locks_Group import the_lock
from The_turtles.The_player import player
from Enemy.The_Enemy_Group import bad_guys


class Level_Creater:
    def __init__(self,level:int,room:int):
        self.backgrounds:dict[tuple,Level_Backgrounds] = {}
        self.level = level
        self.room = room
        self.background = Level_Backgrounds(level,room)
        self.change_rooms(level,room)
        
    def get_background(self,level:int,room:int):
        key = (level, room)
        if key not in self.backgrounds:
            self.backgrounds[key] = Level_Backgrounds(level,room)
        return self.backgrounds[key]
    
    def change_rooms(self, level: int, room: int) -> None:
        self.level = level
        self.room = room
        self.background = self.get_background(level, room)
        bad_guys.get_level_badguys(level, room)
        All_walls.change_level()
        All_walls.load_group(level, room)
        Collect_group.get_level_collectables(level,room)
        the_lock.get_level_lock(level,room)
        

    def handle_collision(self):
        if bad_guys.collision_with_player(player):
            player.died()
    
    def update_level(self,dt:float)->None:
        player.update(dt)
        bad_guys.update(dt)
        Collect_group.update(player)
        the_lock.update(player)
    
    def draw_level(self,screen:pygame.Surface)->None:
        self.background.draw(screen)
        All_walls.draw(screen,player)
        player.draw(screen)
        bad_guys.draw(screen)
        Collect_group.draw(screen)
        the_lock.draw(screen)
        
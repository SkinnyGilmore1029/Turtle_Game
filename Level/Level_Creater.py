import pygame
from Utility.Image_Handler import data
from Utility.Settings import WIDTH, HEIGHT
from .Background_manger import Level_Backgrounds
from .Wall_manger import All_walls
from .Collectables_Group import Collect_group
from .Locks_Group import the_lock
from .Teleporters import The_tele
from .Buttons import Button_group
from The_turtles.The_player import player
from Enemy.The_Enemy_Group import bad_guys
from UI.The_hud import Show_hud

class Level_Creater:
    def __init__(self,level:int,room:int):
        self.backgrounds:dict[tuple,Level_Backgrounds] = {}
        self.level = level
        self.room = room
        self.room2_location = data.get_room2_location(level)
        self.background = Level_Backgrounds(level,room)
        self.change_rooms(level,room)
        
    def get_background(self,level:int,room:int):
        key = (level, room)
        if key not in self.backgrounds:
            self.backgrounds[key] = Level_Backgrounds(level,room)
        return self.backgrounds[key]
        
    def change_up_down(self,game) -> None:
        if self.room2_location == "Above":
            if player.rect.x <= 0:
                player.rect.x = 0
            elif player.rect.x >= WIDTH-64:
                player.rect.x = WIDTH-64
            if player.rect.y <= 0 and game.room == 1:
                game.room +=1
                player.rect.y = HEIGHT -1
                The_tele.get_tele_data(game.level, game.room)
            elif player.rect.y <=0 and game.room == 2:
                player.rect.y =1 
            elif player.rect.y >= HEIGHT and game.room == 2:
                game.room -= 1 
                player.rect.y = 1
                The_tele.get_tele_data(game.level, game.room)
            elif player.rect.y >= HEIGHT-64 and game.room == 1:
                player.rect.y = HEIGHT - 64
    
    #Room 2 on bottom        
    def change_down_up(self,game) -> None:
        if self.room2_location == "Below": 
            if player.rect.x <= 0:
                player.rect.x = 0
            elif player.rect.x >= WIDTH-64:
                player.rect.x = WIDTH-64
            if player.rect.y >= HEIGHT and game.room == 1:
                game.room +=1
                player.rect.y = 1
                The_tele.get_tele_data(game.level, game.room)
            elif player.rect.y <=0 and game.room == 1:
                player.rect.y =1 
            elif player.rect.y <= 0 and game.room ==2:
                game.room -= 1 
                player.rect.y = HEIGHT-32
                The_tele.get_tele_data(game.level, game.room)
            elif player.rect.y >= HEIGHT-32 and game.room == 2:
                player.rect.y = HEIGHT - 32    
    
    def change_left_right(self,game)->None:
        if self.room2_location == "Side":
            if player.rect.y <= 0:
                player.rect.y = 0
            elif player.rect.y >= HEIGHT - 64:
                player.rect.y = HEIGHT-64
            if player.rect.x <= 0 and game.room == 1:
                player.rect.x =1
            elif player.rect.x >= WIDTH-64 and game.room == 2:
                player.rect.x = WIDTH-64
            elif player.rect.x >= WIDTH and game.room == 1:
                game.room +=1
                player.rect.x = 0
                The_tele.get_tele_data(game.level, game.room)
            elif player.rect.x <=0 and game.room ==2:
                game.room -=1         
                player.rect.x = WIDTH-64
                The_tele.get_tele_data(game.level, game.room)
    
    def change_rooms(self, level: int, room: int) -> None:
        self.level = level
        self.room = room
        self.background = self.get_background(level, room)
        self.room2_location = data.get_room2_location(level)
        bad_guys.get_level_badguys(level, room)
        All_walls.change_room()
        All_walls.load_group(level, room)
        Collect_group.get_level_collectables(level,room)
        the_lock.get_level_lock(level,room)
        Button_group.get_level_buttons(level,room)
        

    def clear_level(self):
        Collect_group.empty()
        Collect_group.already_in_level.clear()
        Collect_group.already_collected.clear()
        the_lock.empty()
        the_lock.already_unlocked.clear()
        The_tele.empty()
        bad_guys.empty()
        Button_group.clear_buttons_level()
        
    def handle_collision(self,game:object):
        #Player death
        if bad_guys.collision_with_player(player):
            player.died()
        #Level Win Condition
        if The_tele.collision_with_player(player):
            game.level +=1
            game.room = 1
            player.rect.x = data.get_player_start(game.level)[0]
            player.rect.y = data.get_player_start(game.level)[1]
            self.room2_location = data.get_room2_location(game.level)
    
    def update_level(self,dt:float,game:object)->None:
        player.update(dt)
        bad_guys.update(dt)
        Collect_group.update(player)
        the_lock.update(player)
        The_tele.update()
        self.change_up_down(game)
        self.change_left_right(game)
        self.change_down_up(game)
        if game.level== 2:
            Button_group.update()
        
    def draw_level(self,screen:pygame.Surface,game:object)->None:
        self.background.draw(screen)
        Show_hud(screen,player,self.level,self.room)
        All_walls.draw(screen,player)
        bad_guys.draw(screen)
        Collect_group.draw(screen)
        the_lock.draw(screen)
        The_tele.draw(screen)
        if game.level == 2:
            Button_group.draw(screen)
        player.draw(screen)
import pygame
from Utility.Image_Handler import data
from Utility.Settings import (
    LEVEL1_POS,
    LEVEL2_POS,
    LEVEL3_POS,
    LEVEL4_POS,
    LEVEL5_POS,
    LEVEL6_POS,
    LEVEL7_POS,
    LEVEL8_POS,
    WIDTH,
    HEIGHT
)
from The_turtles.The_player import player
from Enemy.The_Enemy_Group import bad_guys
from UI.The_hud import Show_hud
from NPCS.The_hints import The_hints
from NPCS.The_crabs import The_Crabs
from NPCS.The_Cactus import All_cactus
from NPCS.The_Flies import All_Flies
from NPCS.The_Lizard import Lizards
from .Lily_Pads import All_Lily
from .Background_manger import Level_Backgrounds
from .Wall_manger import All_walls
from .Collectables_Group import Collect_group
from .Locks_Group import the_lock
from .Teleporters import The_tele
from .Buttons import Button_group
from .Heat_Puddle import All_puddles , heat_bar


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
    
    def check_level_only(self,level,room):
        match level:
            case 2:
                Button_group.clear_buttons_room(level,room)
                Button_group.get_level_buttons(level,room)
            case 3:
                The_Crabs.get_level_crabs(level,room)
                All_Lily.change_room()
                All_Lily.get_lily_data(level,room)
            case 4:
                All_cactus.get_level_cactus(level,room)
                All_Flies.get_level_flies(level,room)
                Lizards.get_lizard_data(level,room)
            case 5:
                All_puddles.get_puddle_data(level,room)
                
    
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
        The_hints.get_level_Hints(level,room)
        The_tele.get_tele_data(level,room)
        self.check_level_only(level,room)
                
    def clear_level(self)->None:
        Collect_group.get_clear_level()
        the_lock.clear_level()
        The_tele.empty()
        bad_guys.empty()
        Button_group.clear_buttons_level()
        The_Crabs.clear_level()
        All_walls.moved_walls.clear()
    
    def get_respawn_pos(self)->tuple[int,int]:
        respwn_pos =[0,0]
        match self.level:
            case 1:
                respwn_pos[0] = LEVEL1_POS[0]
                respwn_pos[1] = LEVEL1_POS[1]
            case 2:
                respwn_pos[0] = LEVEL2_POS[0]
                respwn_pos[1] = LEVEL2_POS[1]
            case 3:
                respwn_pos[0] = LEVEL3_POS[0]
                respwn_pos[1] = LEVEL3_POS[1]
            case 4:
                respwn_pos[0] = LEVEL4_POS[0]
                respwn_pos[1] = LEVEL4_POS[1]
            case 5:
                respwn_pos[0] = LEVEL5_POS[0]
                respwn_pos[1] = LEVEL5_POS[1]
            case 6:
                respwn_pos[0] = LEVEL6_POS[0]
                respwn_pos[1] = LEVEL6_POS[1]
            case 7:
                respwn_pos[0] = LEVEL7_POS[0]
                respwn_pos[1] = LEVEL7_POS[1]
            case 8:
                respwn_pos[0] = LEVEL8_POS[0]
                respwn_pos[1] = LEVEL8_POS[1]
                
        return respwn_pos
    
    def handle_collision(self,game:object)->None:
        #Player death
        if bad_guys.collision_with_player(player):
            player_spawn_postion = self.get_respawn_pos()
            player.died(player_spawn_postion)
            self.change_rooms(game.level,game.room)
            game.room = 1
        #Level Win Condition
        collided_tele = The_tele.collision_with_player(player)
        if collided_tele:
            if collided_tele.change_level == True:
                game.level +=1
                game.room = 1
            else:
                game.room = 1
            player.rect.x, player.rect.y = data.get_player_start(game.level)
            self.room2_location = data.get_room2_location(game.level)    
    
    def level_only_update(self,dt,game)->None:
        match game.level:
            case 2:
              Button_group.update()
            case 3:
                The_Crabs.update(dt)
                All_walls.update(dt)
                All_Lily.update(dt)
            case 4:
                All_cactus.update()
                All_Flies.update(dt)
                Lizards.update(dt)
            case 5:
                All_puddles.update()
    
    def update_level(self,dt:float,game:object)->None:
        bad_guys.update(dt)
        Collect_group.update(player)
        the_lock.update(player)
        The_tele.update()
        self.change_up_down(game)
        self.change_left_right(game)
        self.change_down_up(game)
        The_hints.collison_with_player()
        All_walls.update(dt)
        self.level_only_update(dt,game) 
        player.update(dt)
                  
    def draw_level_only(self,screen,game):
        """
        These have json files that other levels
        dont have could mess things up if ran
        together.
        """
        match game.level:
            case 2:
                Button_group.draw(screen)
            case 3:
                The_Crabs.draw(screen)
                All_Lily.draw(screen)
            case 4:
                All_cactus.draw(screen)
                All_Flies.draw(screen)
                Lizards.draw(screen)
            case 5:
                All_puddles.draw(screen)
                heat_bar.draw(screen)
        
        
    def draw_level(self,screen:pygame.Surface,game:object)->None:
        self.background.draw(screen)
        All_walls.draw(screen)
        bad_guys.draw(screen)
        Collect_group.draw(screen)
        the_lock.draw(screen)
        The_tele.draw(screen)
        The_hints.draw(screen)
        self.draw_level_only(screen,game)
        player.draw(screen)
        Show_hud(screen,player,self.level,self.room)
import pygame
from Managers.Data_Manager import data
from Utility.Settings import (
    LEVEL1_POS,
    LEVEL2_POS,
    LEVEL3_POS,
    LEVEL4_POS,
    LEVEL5_POS,
    LEVEL6_POS,
    LEVEL7_POS,
    LEVEL8_POS,
)
from The_turtles.The_player import player

from Enemy.The_Enemy_Group import bad_guys

from UI.The_hud import Show_hud

from NPCS.The_crabs import The_Crabs

from Managers.Background_manager import Level_Backgrounds
from Managers.Wall_manager import All_walls
from Managers.Room_Manager import Room_Handler
from .Check_Points import Check_point
from .Collectables_Group import Collect_group
from .Locks_Group import the_lock
from .Teleporters import The_tele
from .Buttons import Button_group
from .shelter import The_shelters


class Level_Creater:
    def __init__(self,level:int,room:int):
        self.backgrounds:dict[tuple,Level_Backgrounds] = {}
        self.The_Rooms:Room_Handler =Room_Handler(room,level)
        self.level = self.The_Rooms.level
        self.room: int = self.The_Rooms.room

        self.background = Level_Backgrounds(level,room)
        #load the first room
        self.change_rooms(level,room)

    def draw_starting_square(self, screen:pygame.Surface) ->None:
        match self.level:
            case 1:
                x, y = LEVEL1_POS
                color = "#FFFFFF"
            case 2:
                x, y = LEVEL2_POS
                color = "#1D2969"
            case 3:
                x, y = LEVEL3_POS
                color = "#E71313"
            case 4:
                x, y = LEVEL4_POS
                color = "#5DEE39"
            case 5:
                x, y = LEVEL5_POS
                color = "#70294D"
            case 6:
                x, y = LEVEL6_POS
                color = "#23C790"
            case 7:
                x, y = LEVEL7_POS
                color = "#344223"
            case 8:
                x, y = LEVEL8_POS
                color = "#280A41"
        pygame.draw.rect(screen,color,(x, y,player.w,player.h))

    def get_background(self,level:int,room:int):
        key = (level, room)
        if key not in self.backgrounds:
            self.backgrounds[key] = Level_Backgrounds(level,room)
        return self.backgrounds[key]

    def change_rooms(self, level: int, room: int) -> None:
        self.level = level
        self.room = room
        self.background = self.get_background(level, room)
        self.The_Rooms.room2_location = data.get_room2_location(level)
        self.The_Rooms.change_rooms(level, room)

    def clear_level(self)->None:
        Collect_group.get_clear_level()
        the_lock.clear_level()
        The_tele.empty()
        bad_guys.empty()
        Button_group.clear_buttons_level()
        The_Crabs.clear_level()
        All_walls.moved_walls.clear()
        The_shelters.change_level()
        Check_point.empty_cp()

    def get_respawn_pos(self)->tuple[int,int]:
        respwn_pos =[0,0]
        if not Check_point.sprite.acquired:
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
        elif Check_point.sprite.acquired:
            respwn_pos[0] = Check_point.sprite.rect.x
            respwn_pos[1] = Check_point.sprite.rect.y
        return respwn_pos

    def handle_collision_death(self,game:object)->None:
        #Player death
        if bad_guys.collision_with_player(player):
            player_spawn_postion = self.get_respawn_pos()
            player.died(player_spawn_postion)

            if not Check_point.sprite.acquired:
                game.room = 1
            elif Check_point.sprite.acquired:
                game.room = 2
            self.change_rooms(game.level,game.room)

    def handle_collision_winning(self, game:object) -> None:
        #Level Win Condition
        collided_tele = The_tele.collision_with_player(player)
        if collided_tele:
            if collided_tele.change_level == True:
                game.level +=1
                game.room = 1
                self.The_Rooms.change_level((game.level))
                player.rect.x, player.rect.y = data.get_player_start(game.level)
                self.room2_location = data.get_room2_location(game.level)
            elif game.level ==3:
                game.room = 1
                player.rect.x, player.rect.y =  data.get_player_start(game.level)
            elif game.level == 7:
                game.room = 2
                player.rect.x, player.rect.y = (10, 400)


    def update_level(self,dt:float,game:object)->None:
        self.The_Rooms.update(dt, game)
        player.update(dt)


    def draw_level(self,screen:pygame.Surface,game:object)->None:
        self.background.draw(screen)
        self.The_Rooms.draw(screen)
        if self.room == 1:
            self.draw_starting_square(screen)
        player.draw(screen)
        Show_hud(screen,player,self.level,self.room)
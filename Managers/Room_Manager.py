import pygame
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
from Enemy.The_Villian import boss2
from The_turtles.Jesse import jesse2
from Enemy.The_Enemy_Group import bad_guys
from Enemy.The_Bolders import final_bolder
from NPCS.The_hints import The_hints
from NPCS.The_crabs import The_Crabs
from NPCS.The_Cactus import All_cactus
from NPCS.The_Flies import All_Flies
from NPCS.The_Lizard import Lizards
from .Wall_manager import All_walls
from Level.Lily_Pads import All_Lily
from Level.Collectables_Group import Collect_group
from Level.Locks_Group import the_lock
from Level.Teleporters import The_tele
from Level.Buttons import Button_group
from Level.Heat_Puddle import All_puddles , heat_bar
from Level.shelter import The_shelters
from Managers.Data_Manager import data

class Room_Handler:
    def __init__(self,room:int, level:int) -> None:
        self.room: int = room
        self.level: int = level
        self.change_direction: str = ""
        self.spawn_positions: dict[str,list[tuple[int,int]]] = {
            "Level 1" : [LEVEL1_POS],
            "Level 2" : [LEVEL2_POS],
            "Level 3" : [LEVEL3_POS],
            "Level 4" : [LEVEL4_POS],
            "Level 5" : [LEVEL5_POS],
            "Level 6" : [LEVEL6_POS],
            "Level 7" : [LEVEL7_POS],
            "Level 8" : [LEVEL8_POS],
        }
        self.room2_location = data.get_room2_location(level)

    def change_level(self, new_level:int)-> None:
        """Responsible for changing the level for
        the room handler.

        Args:
            new_level (int): Level you want to change to.
        """
        self.level = new_level

    def change_room(self, new_room:int) -> None:
        """Responsible for changing the room for
        the room handler.

        Args:
            new_room (int): Room you want to change to.
        """
        self.room = new_room

    def get_current_level(self)->int:
        """Get the current level to keep
        the game up to date.

        Returns:
            int: The current level.
        """
        return self.level

    def get_current_room(self) -> int:
        """Get the current room to keep
        the game up to date.

        Returns:
            int: The current room.
        """
        return self.room

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

    def unique_to_room_draw(self, screen:pygame.Surface)-> None:
        """Responsible for draw things on the screen that
        are unique to the level or the room.

        Args:

            screen (pygame.Surface): The main screen to draw on.
        """
        match self.level:
            case 1:
                pass
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
            case 6:
                The_shelters.draw(screen)
            case 7:
                Button_group.draw(screen)
            case 8:
                Button_group.draw(screen)
                if self.room == 2:
                    boss2.draw(screen)
                    jesse2.draw(screen)
                    final_bolder.draw_final(screen)

    def load_unique_to_room(self,level:int, room:int)->None:
        """Loads things that are unique to each room and or level.

        Args:
            level (int): The current level
        """
        match level:
            case 1:
                pass
            case 2:
                Button_group.clear_buttons_room(level,room)
                Button_group.get_level_buttons(level,room)
            case 3:
                The_Crabs.get_level_crabs(level, room)
                All_Lily.change_room()
                All_Lily.get_lily_data(level, room)
            case 4:
                All_cactus.get_level_cactus(level,room)
                All_Flies.get_level_flies(level,room)
                Lizards.get_lizard_data(level,room)
            case 5:
                All_puddles.get_puddle_data(level,room)
            case 6:
                The_shelters.get_shelter_data(level,room)
            case 7:
                Button_group.clear_buttons_room(level,room)
                Button_group.get_level_buttons(level,room)
            case 8:
                Button_group.clear_buttons_room(level,room)
                Button_group.get_level_buttons(level,room)

    def unique_only_updates(self, dt:float, game:object) -> None:
        """Responsible for updating things unique to certain
        levels and rooms.

        Args:
            dt (float): Delta Time variable.
            game (object): Main Class that runs the game.
        """
        match game.level:
            case 2:
                Button_group.update()
            case 3:
                The_Crabs.update(dt)
                All_Lily.update(dt)
            case 4:
                All_cactus.update()
                All_Flies.update(dt)
                Lizards.update(dt)
            case 5:
                All_puddles.update()
            case 6:
                The_shelters.update()
            case 7:
                Button_group.update()
            case 8:
                Button_group.update()
                if game.room == 2:
                    boss2.update(dt)
                    jesse2.update(player,game)
                    final_bolder.final_update(All_walls.get_wall_by_name("Cage Front"),dt)

    def win_condition(self, level:int, room:int)-> None:
        """Responsible for loading in the Teleporters
        that take you to the next level

        Args:
            level (int): The current level.
            room (int): The current room.
        """

        The_tele.get_tele_data(level,room)

    def room_walls(self, level:int, room:int) -> None:
        """Responsible for loading in the correct
        walls for the rooms in the level.

        Args:
            level (int): The current level
            room (int): The current room
        """
        All_walls.change_room()
        All_walls.load_group(level, room)

    def room_hints(self, level:int, room:int) -> None:
        """Responsible for loading the correct hint frogs for the
        room and level.

        Args:
            level (int): The current level.
            room (int): The current room.
        """

        The_hints.get_level_Hints(level, room)

    def room_monsters(self, level:int, room:int) -> None:
        """Responsible for loading in the correct
        monsters for the level and rooms.

        Args:
            level (int): The current level
            room (int): The current room
        """

        bad_guys.get_level_badguys(level, room)

    def room_collectables(self, level:int, room:int) -> None:
        """Responsible for loading in the keys
        and one ups for the correct level and rooms.

        Args:
            level (int): The current level
            room (int): The current room
        """

        Collect_group.get_level_collectables(level,room)

    def room_locks(self, level:int, room:int) -> None:
        """Responsible for loading in the Locks
        for the correct level and rooms.

        Args:
            level (int): The current level
            room (int): The current room
        """

        the_lock.get_level_lock(level,room)

    def change_rooms(self, level:int, room:int)-> None:
        """Responsible for handling the loading and changing
        between room switching.

        Args:
            level (int): Level to change to.
            room (int): Room to change to.
        """
        self.load_unique_to_room(level, room)
        self.room_walls(level,room)
        self.room_collectables(level,room)
        self.room_monsters(level, room)
        self.room_locks(level,room)
        self.win_condition(level, room)
        self.room_hints(level, room)

    def tele_second_room(self):
        if self.room2_location == "Tele":
            if player.rect.y <= 0:
                player.rect.y = 0
            elif player.rect.y >= HEIGHT - 64:
                player.rect.y = HEIGHT-64
            if player.rect.x <= 0:
                player.rect.x = 0
            elif player.rect.x >= WIDTH-64:
                player.rect.x = WIDTH-64

    def update(self, dt:float, game:object) -> None:
        """Updates the Room_handler to keep everything up to date.
        """

        bad_guys.update(dt)
        Collect_group.update(player)
        the_lock.update(player)
        The_tele.update()
        self.change_up_down(game)
        self.change_left_right(game)
        self.change_down_up(game)
        self.tele_second_room()
        The_hints.collison_with_player()
        All_walls.update(dt)
        self.unique_only_updates(dt, game)

    def draw(self, screen: pygame.Surface)-> None:
        """Puts everything on the screen.

        Args:
            screen (pygame.Surface): The main draw window.
        """
        self.unique_to_room_draw(screen)
        All_walls.draw(screen)
        bad_guys.draw(screen)
        Collect_group.draw(screen)
        the_lock.draw(screen)
        The_tele.draw(screen)
        The_hints.draw(screen)
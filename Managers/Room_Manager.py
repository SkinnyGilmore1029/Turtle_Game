import pygame
from Managers.Image_Manager import data
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
from UI.The_hud import Show_hud
from NPCS.The_hints import The_hints
from NPCS.The_crabs import The_Crabs
from NPCS.The_Cactus import All_cactus
from NPCS.The_Flies import All_Flies
from NPCS.The_Lizard import Lizards
from .Background_manager import Level_Backgrounds
from .Wall_manager import All_walls
from Level.Lily_Pads import All_Lily
from Level.Collectables_Group import Collect_group
from Level.Locks_Group import the_lock
from Level.Teleporters import The_tele
from Level.Buttons import Button_group
from Level.Heat_Puddle import All_puddles , heat_bar
from Level.shelter import The_shelters

class Room_Handler:
    def __init__(self,room:int, level:int) -> None:
        self.room: int = room
        self.level: int = room

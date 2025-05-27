import pygame
from .Screen_base import Screens
from The_turtles.The_player import player
from Utility.Settings import (
    LEVEL1_POS,
    LEVEL2_POS,
    LEVEL3_POS,
    LEVEL4_POS,
    LEVEL5_POS,
    LEVEL6_POS,
    LEVEL7_POS,
    LEVEL8_POS
)

class Choose_Level(Screens):
    def __init__(self,name:str)->None:
        super().__init__(name)
    
    def choosing_level(self,game:object,dt)->None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            game.level = 1
            game.playing = True
            game.game_state = "Playing"
            player.rect.x = LEVEL1_POS[0]
            player.rect.y = LEVEL1_POS[1]
            
        elif keys[pygame.K_2]:
            game.level = 2
            game.playing = True
            game.game_state = "Playing"
            player.rect.x = LEVEL2_POS[0]
            player.rect.y = LEVEL2_POS[1]
        
        elif keys[pygame.K_3]:
            game.level = 3
            game.playing = True
            game.game_state = "Playing"
            player.rect.x = LEVEL3_POS[0]
            player.rect.y = LEVEL3_POS[1]
            

        elif keys[pygame.K_4]:
            game.level = 4
            game.playing = True
            game.game_state = "Playing"
            player.rect.x = LEVEL4_POS[0]
            player.rect.y = LEVEL4_POS[1]
        """
        elif keys[pygame.K_5]:
            game.level = 5
            game.playing = True
            game.game_state = "Playing"
            player.rect.x = LEVEL5_POS[0]
            player.rect.y = LEVEL5_POS[1]

        elif keys[pygame.K_6]:
            game.level = 6
            game.playing = True
            game.game_state = "Playing"
            player.rect.x = LEVEL6_POS[0]
            player.rect.y = LEVEL6_POS[1]

        elif keys[pygame.K_7]:
            game.level = 7
            game.playing = True
            game.game_state = "Playing"
            player.rect.x = LEVEL7_POS[0]
            player.rect.y = LEVEL7_POS[1]
            
        elif keys[pygame.K_8]:
            game.level = 8
            game.playing = True
            game.game_state = "Playing"
            player.rect.x = LEVEL8_POS[0]
            player.rect.y = LEVEL8_POS[1]
            """
        
    def draw_choose_level_screen(self,screen:pygame.Surface)->None:
        screen.fill("Blue")
        Instruction = self.fonts["Title"].render("Choose Your Level!",True,"#F5E800")
        level1 = self.fonts["Start Button"].render("Level 1: press 1",True,"#F5E800")
        level2 = self.fonts["Start Button"].render("Level 2: press 2",True,"#F5E800")
        level3 = self.fonts["Start Button"].render("Level 3: press 3",True,"#F5E800")
        level4 = self.fonts["Start Button"].render("Level 4: press 4",True,"#F5E800")
        level5 = self.fonts["Start Button"].render("Level 5: press 5",True,"#F5E800")
        level6 = self.fonts["Start Button"].render("Level 6: press 6",True,"#F5E800")
        level7 = self.fonts["Start Button"].render("Level 7: press 7",True,"#F5E800")
        level8 = self.fonts["Start Button"].render("Level 8: press 8",True,"#F5E800")
        """
        
            
            (level5,(200,360)),
            (level6,(200,400)),
            (level7,(200,440)),
            (level8,(200,480))
        """
        screen.blits([
            (Instruction,(400,0)),
            (level1,(200,200)),
            (level2,(200,240)),
            (level3,(200,280)),
            (level4,(200,320)),
        ])
        
Choosing_screen = Choose_Level('Title Screen')
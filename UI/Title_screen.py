import pygame
from .Screen_base import Screens
from Utility.Image_Handler import data
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

       
class Title(Screens):
    def __init__(self,name:str)->None:
        super().__init__(name)
        self.background = data.load_image(name)
        
    def begin_game(self,game:object)->None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            game.playing = True
            game.game_state = "Starting Cutscene"
        
    def choose_level(self,game:object)->None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_l]:
            game.game_state = "Choosing Level"
            
            
    def choosing_level(self,game:object)->None:
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
        
        """ elif keys[pygame.K_3]:
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
    
    def Title_screen_text(self,screen:pygame.Surface):
        Title = self.fonts["Title"].render("Squartle Quest!",True,"#F5E800")
        Start_button = self.fonts["Start Button"].render("Press S to start your quest!",True,"#F5E800")
        or_text = self.fonts["Start Button"].render("OR",True,"#F5E800")
        Level_select = self.fonts["Start Button"].render("Press L to select a Level to start from!", True , "#F5E800")
        screen.blits([
            (Title,(240,40)),
            (Start_button,(100,640)),
            (or_text,(200,675)),
            (Level_select,(100,710))
            ])
        
    def draw_Title_screen(self,screen:pygame.Surface,game:object)->None:
        screen.blit(self.background,(0,0))
        self.begin_game(game)
        self.choose_level(game)
        self.Title_screen_text(screen)
        
    def draw_choose_level_screen(self,screen:pygame.Surface,game:object)->None:
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
        (level3,(200,280)),
            (level4,(200,320)),
            (level5,(200,360)),
            (level6,(200,400)),
            (level7,(200,440)),
            (level8,(200,480))
        """
        screen.blits([
            (Instruction,(400,0)),
            (level1,(200,200)),
            (level2,(200,240)),
            
        ])


Title_screen = Title('Title Screen')
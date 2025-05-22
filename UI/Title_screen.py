import pygame
from .Screen_base import Screens
from Utility.Image_Handler import data

       
class Title(Screens):
    def __init__(self,name:str)->None:
        super().__init__(name)
        self.background = data.load_image(name)
        
    def begin_game(self,game):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            game.playing = True
            game.game_state = "Starting Cutscene"
        
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
        
    def draw_Title_screen(self,screen:pygame.Surface,game)->None:
        screen.blit(self.background,(0,0))
        self.begin_game(game)
        self.Title_screen_text(screen)


Title_screen = Title('Title Screen')
import pygame
from .Screen_base import Screens
from The_turtles.The_player import player
import sys


class Win_Screen(Screens):
    def __init__(self,name:str):
        super().__init__(name)
    
    def choose_level_again(self,game)->None:
        player.lives = 15
        game.game_state = "Choosing Level"
    
    def go_title(self,game)->None:
        game.game_state = "Title Screen"

    def controls(self,game):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_l]:
            self.choose_level_again(game)
        if keys[pygame.K_t]:
            self.go_title(game)
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

    def draw(self,screen:pygame.Surface)->None:
        screen.fill("Blue")
        win_text = self.fonts["Title"].render("You Win!",True,"#FFFB00")
        continue_text = self.fonts["Start Button"].render("Press L to choose level again.",True,"#FFFB00")
        title_text = self.fonts["Start Button"].render("Press T to go to title screen.",True,"#FFFB00")

        screen.blits([
            (win_text,(400,0)),
            (continue_text,(300,700)),
            (title_text,(300,750))
        ])

Win = Win_Screen("Win Screen")
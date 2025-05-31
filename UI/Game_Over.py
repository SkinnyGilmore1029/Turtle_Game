import pygame 
from .Screen_base import Screens
from The_turtles.The_player import player


class GameOver(Screens):
    def __init__(self,name:str):
        super().__init__(name)
        
    def check_lives(self,game)->None:
        if player.lives <= 0:
            game.game_state = "Game Over"
            game.playing = False
            

    def Game_over_text(self,screen:pygame.Surface)->None:
        game_over = self.fonts['Title'].render("Squartle Died",True,"#372BDFF8")
        continue_text = self.fonts['Start Button'].render("Press C to continue from where you died.",True,"#372BDFF8")
        Level_select = self.fonts["Start Button"].render("Press L to select a Level to start from!", True , "#372BDFF8")
        
        screen.blits([
            (game_over,(400,0)),
            (continue_text,(300,700)),
            (Level_select,(300,750))
        ])
        
    def continue_from(self,game)-> None:
        player.lives = 5
        game.game_state = "Playing"
        game.playing = True
        
    def choose_level_again(self,game)->None:
        player.lives = 5
        game.game_state = "Choosing Level"
        
    def game_over_controls(self,game)->None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_c]:
            self.continue_from(game)
        elif keys[pygame.K_l]:
            self.choose_level_again(game)
        
    def draw_game_over_screen(self,screen:pygame.Surface):
        screen.fill("#F31313")
        self.Game_over_text(screen)
        
Game_over_screen = GameOver("GameOver")
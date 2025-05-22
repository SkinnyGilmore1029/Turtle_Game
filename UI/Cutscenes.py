import pygame
from Utility.Image_Handler import data
from The_turtles.Jesse import jesse
from The_turtles.The_player import player
from Enemy.The_Enemies import boss
from .Screen_base import Screens

class CutScenes(Screens):
    def __init__(self,name:str)->None:
        super().__init__(name)
        self.background = data.load_image(name)
        
    def capture_turtle(self,dt)->None:
        jesse.getting_captured(player,boss,dt)
        
    def draw(self,screen:pygame.Surface)->None:
        screen.blit(self.background,(0,0))
        
    def Starting_cutscene(self,screen,game,dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            game.game_state = "Playing"
        self.draw(screen)    
        self.capture_turtle(dt)
        jesse.draw(screen)
        
Cut_scenes = CutScenes("Starting Scene")
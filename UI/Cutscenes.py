import pygame
from Utility.Image_Handler import data
from .Screen_base import Screens

class CutScenes(Screens):
    def __init__(self,name:str)->None:
        super().__init__(name)
        self.background = data.load_image(name)
    
    def start_game(self,game):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            game.game_state = "Playing"
    
    def draw(self,screen:pygame.Surface)->None:
        screen.blit(self.background,(0,0))
        
Cut_scenes = CutScenes("Starting Scene")
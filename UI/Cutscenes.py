import pygame
from Utility.Image_Handler import data
from .Screen_base import Screens

class CutScenes(Screens):
    def __init__(self,name:str)->None:
        super().__init__(name)
        self.background = data.load_image(name)
        
        
    def Starting_cutscene(self,screen,game,dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            game.game_state = "Playing"
        screen.blit(self.background,(0,0))
        
Cut_scenes = CutScenes("Starting Scene")
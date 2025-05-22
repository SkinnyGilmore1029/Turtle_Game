import pygame
from Utility.Image_Handler import data
from .Screen_base import Screens
from The_turtles.The_player import player
from The_turtles.Jesse import jesse
from Enemy.The_Enemies import boss

class CutScenes(Screens):
    def __init__(self,name:str)->None:
        super().__init__(name)
        self.background = data.load_image(name)

    def start_game(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_RETURN]:
            player.chase = True

    def update(self,dt,game):
        player.update_cutscene(dt,game)
        jesse.update_cutscene(dt,boss,player)
        boss.update_cutscene(jesse,dt)
        
    def draw(self,screen:pygame.Surface):
        screen.blit(self.background,(0,0))
        player.draw(screen)
        jesse.draw(screen)
        boss.draw(screen)
        
Cut_scenes = CutScenes("Starting Scene")
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
        self.font = pygame.font.SysFont("Arial",48,True)

    def start_game(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_RETURN]:
            player.chase = True

    def Cut_scene1_text(self,screen:pygame.Surface):
        if jesse.follow == False and player.chase == False:
            text = self.font.render("One day while Squartle is chilling with his friend",True,"Black","Light Blue",1200)
        elif jesse.follow == True and player.chase == False:
            text = self.font.render("Some wierd creature comes out of no where and takes Squartle friend!",True,"Black","Light Blue",1200)
        elif jesse.follow == True and player.chase == True:
            text = self.font.render("Now begins his journey to save his friend!",True,"Black","Light Blue",1200)
        screen.blit(text,(0,0))

    def update(self,dt,game):
        player.update_cutscene(dt,game)
        jesse.update_cutscene(dt,boss,player)
        boss.update_cutscene(jesse,dt)
        
    def draw(self,screen:pygame.Surface):
        screen.blit(self.background,(0,0))
        self.Cut_scene1_text(screen)
        player.draw(screen)
        jesse.draw(screen)
        boss.draw(screen)
        
Cut_scenes = CutScenes("Starting Scene")
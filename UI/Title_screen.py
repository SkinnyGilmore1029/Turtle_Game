import pygame
from The_turtles.Jesse import jesse
from Enemy.The_Enemies import boss
from Utility.Image_Handler import data

class Screens:
    def __init__(self,name:str):
        self.name = name
        self.background = data.load_image(name)
        self.fonts:dict = {
            "Title" : pygame.font.SysFont("Arial",48,True),
            "Start Button" : pygame.font.SysFont("Arial",32,True)
        }
     
    def begin_game(self,game):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            game.playing = True
            game.game_state = "Starting Cutscene"
            self.change_scene('Starting Scene')
    
    def change_scene(self,new_name:str)->None:
        self.name = new_name
        self.background = data.load_image(new_name)
       
    def Title_screen_text(self,screen:pygame.Surface):
        Title = self.fonts["Title"].render("Squartle Quest!",True,"#F5E800")
        Start_button = self.fonts["Start Button"].render("Press S to start your quest!",True,"#F5E800")
        screen.blits([(Title,(240,40)),(Start_button,(100,640))])
        
    def draw_Title_screen(self,screen:pygame.Surface,game)->None:
        screen.blit(self.background,(0,0))
        self.begin_game(game)
        self.Title_screen_text(screen)
        
    def capture_turtle(self,screen:pygame.Surface,dt):
        jesse.update(dt)
        jesse.draw(screen)
        
    def Starting_cutscene(self,screen,game,dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            game.game_state = "Playing"
        screen.blit(self.background,(0,0))
        self.capture_turtle(screen,dt)
        
Title_screen = Screens('Title Screen')
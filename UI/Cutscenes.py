import pygame
from Utility.Image_Handler import data
from .Screen_base import Screens
from The_turtles.The_player import Player
from The_turtles.Jesse import Jesse
from Enemy.The_Enemies import Main_Boss

class CutScenes(Screens):
    def __init__(self,name:str)->None:
        super().__init__(name)
        self.background = data.load_image(name)
        self.cutscene_sprites:dict = {
            "Green Turtle 1" : (self.get_cutscene1_data("player"),Player),
            "Pink Turtle 1" : (self.get_cutscene1_data("Jesse"),Jesse),
            "Boss" : (self.get_cutscene1_data("Boss"),Main_Boss)
        }
        self.green_turtle = self.create_sprites("Green Turtle 1")
        self.pink_turtle = self.create_sprites("Pink Turtle 1")
        self.main_boss = self.create_sprites("Boss")
        self.update()
    
    def get_cutscene1_data(self,who:str)->dict:
        return data.from_cutscene_json()["Cut Scene1"][who]
    
    def create_sprites(self,name:str)->object:
        clas = self.cutscene_sprites[name][1]
        if clas:
            if name != "Boss":
                return clas(
                    name= self.cutscene_sprites[name][0]['name'],
                    x= self.cutscene_sprites[name][0]['x'],
                    y= self.cutscene_sprites[name][0]['y'],
                    width= self.cutscene_sprites[name][0]['width'],
                    height= self.cutscene_sprites[name][0]['height'],
                    direction= self.cutscene_sprites[name][0]['direction'],
                    frame_count = self.cutscene_sprites[name][0]['frame_count']
                )
            elif name == "Boss":
                return clas(
                    name= self.cutscene_sprites[name][0]['name'],
                    x= self.cutscene_sprites[name][0]['x'],
                    y= self.cutscene_sprites[name][0]['y'],
                    width= self.cutscene_sprites[name][0]['width'],
                    height= self.cutscene_sprites[name][0]['height'],
                    direction= self.cutscene_sprites[name][0]['direction'],
                    frame_count= self.cutscene_sprites[name][0]['frame_count'],
                    in_room= 0,
                    speed= self.cutscene_sprites[name][0]['speed']
                )
    
    def green_turtle_update(self):
        #self.green_turtle.image = None
        #self.green_turtle.image = data.load_image("Turtle")
        self.green_turtle.image = pygame.transform.smoothscale(self.green_turtle.image,(self.green_turtle.w,self.green_turtle.y))
        self.green_turtle.rect = pygame.Rect(self.green_turtle.x,self.green_turtle.y,self.green_turtle.w,self.green_turtle.h)
        self.green_turtle.mask = pygame.mask.from_surface(self.green_turtle.image)
        print("updated green")
    
    def pink_turtle_update(self):
        #self.pink_turtle.image = None
        #self.pink_turtle.image = data.load_image("Turtle2")
        self.pink_turtle.image = pygame.transform.smoothscale(self.pink_turtle.image,(self.pink_turtle.w,self.pink_turtle.h))
        self.pink_turtle.rect = pygame.Rect(self.pink_turtle.x,self.pink_turtle.y,self.pink_turtle.w,self.pink_turtle.h)
        self.pink_turtle.mask = pygame.mask.from_surface(self.pink_turtle.image)
        print("updated pink")
        
    def boss_update(self):
        #self.main_boss.image = None
        #self.main_boss.image = data.load_image("Boss")
        self.main_boss.image = pygame.transform.smoothscale(self.main_boss.image,(self.main_boss.w,self.main_boss.h))
        self.main_boss.rect = pygame.Rect(self.main_boss.x,self.main_boss.y,self.main_boss.w,self.main_boss.h)
        self.main_boss.mask = pygame.mask.from_surface(self.main_boss.image)
        print("updated boss")
    
    def update(self):
        self.green_turtle_update()
        self.pink_turtle_update()
        self.boss_update()
    
    def start_game(self,game):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            game.game_state = "Playing"
    
    def draw(self,screen:pygame.Surface)->None:
        screen.blits([
            (self.background,(0,0)),
            (self.green_turtle.image,self.green_turtle.rect),
            (self.pink_turtle.image,self.pink_turtle.rect),
            (self.main_boss.image,self.main_boss.rect)
            ])
        
        
        
Cut_scenes = CutScenes("Starting Scene")
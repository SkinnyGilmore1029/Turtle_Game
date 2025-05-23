import pygame
from .Turtle_base import Turtle_Base
from Utility.Settings import HEIGHT

class Jesse(Turtle_Base):
    def __init__(self,name:str,x:float,y:float,width:int,height:int,direction:str,frame_count:int,sheet_size:list):
        super().__init__(name,x,y,width,height,direction,frame_count,sheet_size)
        self.scaled = False
        self.follow = False
    
    def move_cutscene(self,dt,boss,player):
        self.velocity.y = 0
        if pygame.sprite.collide_mask(self,boss):
            self.follow = True
        if self.follow == True:
            self.velocity.y = 150
        self.rect.y += self.velocity.y *dt
        
        if self.rect.y > HEIGHT:
            player.chase = True
            self.rect.y = HEIGHT
     
    def update(self):
        self.handle_animations()
        
    def update_cutscene(self,dt,boss,player):
        self.name = "Turtle 2"
        self.move_cutscene(dt,boss,player)
        self.handle_animations()
    
    def draw(self,screen:pygame.Surface)->None:
        screen.blit(self.image,self.rect)
    
jesse = Jesse("Turtle 2",472,210,64,64,"Up",3,[714,247])

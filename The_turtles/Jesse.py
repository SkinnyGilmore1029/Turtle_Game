import pygame
from .Turtle_base import Turtle_Base

class Jesse(Turtle_Base):
    def __init__(self,name:str,x:float,y:float,width:int,height:int,direction:str,frame_count:int):
        super().__init__(name,x,y,width,height,direction,frame_count)
        self.scaled = False
        self.follow = False
        
    def update(self):
        self.handle_animations()
    
    def draw(self,screen:pygame.Surface)->None:
        screen.blit(self.image,self.rect)
    
jesse = Jesse("Turtle2",472,210,64,64,"Up",6)

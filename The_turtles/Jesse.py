import pygame
from .The_player import Player

class Jesse(Player):
    def __init__(self,name:str,x:float,y:float,width:int,height:int,direction:str,frame_count:int):
        super().__init__(name,x,y,width,height,direction,frame_count)
    
    def move(self,dt):
        pass
    
    def draw(self,screen:pygame.Surface):
        screen.blit(self.image,self.rect)
        
jesse = Jesse("Turtle2",600,400,64,64,"Down",6)

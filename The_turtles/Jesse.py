import pygame
from .The_player import Player
from Utility.Image_Handler import data


class Jesse(Player):
    def __init__(self,name:str,x:float,y:float,width:int,height:int,direction:str,frame_count:int):
        super().__init__(name,x,y,width,height,direction,frame_count)
        
    def jesse_still_image(self):
        self.image = data.load_image(self.name)
        self.rect = pygame.FRect(self.x,self.y,self.w,self.h)
    
jesse = Jesse("Turtle2",600,400,64,64,"Up",6)

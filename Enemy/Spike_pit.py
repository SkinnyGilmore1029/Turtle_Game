import pygame
from .Bad_Guy_Base import Bad_guy


class The_spikes(Bad_guy):
    def __init__(self,name:str,x:float,y:float,width:int,height:int,direction:str,frame_count:int,in_room:int,speed:list,sheet_size:list)->None:
        super().__init__(name,x,y,width,height,direction,frame_count,in_room,speed,sheet_size)
        self.start_pos = (x,y)

    def update(self,dt):
        pass

    def draw(self,screen:pygame.Surface):
        screen.blit(self.image,self.rect)
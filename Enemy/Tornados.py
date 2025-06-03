import pygame
from .Bad_Guy_Base import Bad_guy


class Tornado(Bad_guy):
    def __init__(self,name:str,x:float,y:float,width:int,height:int,direction:str,frame_count:int,in_room:int,speed:list,sheet_size:list)->None:
        super().__init__(name,x,y,width,height,direction,frame_count,in_room,speed,sheet_size)
        
    def move(self,dt):
        self.rect.x += self.speed[0] * dt
        self.rect.y += self.speed[1] * dt
    
    def update(self,dt):
        self.move(dt)
        self.handle_animations()
        
    def draw(self,screen)->None:
        screen.blit(self.image,self.rect)
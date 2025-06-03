import pygame
from .Bad_Guy_Base import Bad_guy


class Tornado(Bad_guy):
    def __init__(self,name:str,x:float,y:float,width:int,height:int,direction:str,frame_count:int,in_room:int,speed:list,sheet_size:list)->None:
        super().__init__(name,x,y,width,height,direction,frame_count,in_room,speed,sheet_size)
        
    def move(self,dt):
        self.rect.x += self.speed[0] * dt
        self.rect.y += self.speed[1] * dt
        
    def check_borders(self):
        if self.rect.x <= 0 or self.rect.x >= 1200-self.w:
            self.speed[0] *= -1
        if self.rect.y <=0 or self.rect.y >= 800 - self.h:
            self.speed[1] *= -1
    
    def update(self,dt):
        self.check_borders()
        self.move(dt)
        self.handle_animations()
        
    def draw(self,screen)->None:
        screen.blit(self.image,self.rect)
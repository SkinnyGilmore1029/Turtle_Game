import pygame
from .Bad_Guy_Base import Bad_guy

class The_Rats(Bad_guy):
    def __init__(self,name:str,x:float,y:float,width:int,height:int,direction:str,frame_count:int,in_room:int,speed:list,sheet_size:list)->None:
        super().__init__(name,x,y,width,height,direction,frame_count,in_room,speed,sheet_size)
        self.start_pos = (x,y)
        
        
    def move(self,dt)->None:
        self.rect.y += self.velocity.y * dt
        self.rect.x -= self.velocity.x * dt
        if self.rect.y <= 0 or self.rect.y >= 800 - self.h:
            self.velocity.y *= -1
        if self.rect.x <= 0 or self.rect.x >= 1200 - self.w:
            self.velocity.x *= -1
    
    def update(self,dt)->None:
        self.move(dt)
        self.handle_animations()
        
    def draw(self,screen:pygame.Surface)->None:
        screen.blit(self.image,self.rect)
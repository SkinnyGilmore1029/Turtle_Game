import pygame
from .Bad_Guy_Base import Bad_guy


class The_Scorpion(Bad_guy):
    def __init__(self,name:str,x:float,y:float,width:int,height:int,direction:str,frame_count:int,in_room:int,speed:list,sheet_size:list)->None:
        super().__init__(name,x,y,width,height,direction,frame_count,in_room,speed,sheet_size)
        
    
    def move(self,dt):
        if self.direction == "Up" or self.direction == "Down":
            self.rect.y += self.velocity.y *dt
        elif self.direction == "Left" or self.direction == "Right":
            self.rect.x += self.velocity.x *dt
        
    
    def update(self,dt)->None:
        self.move(dt)
        self.handle_animations()
    
    def draw(self,screen:pygame.Surface)->None:
        screen.blit(self.image,self.rect)
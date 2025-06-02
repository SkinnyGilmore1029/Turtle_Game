import pygame
from Utility.Settings import WIDTH
from .Bad_Guy_Base import Bad_guy

class The_cars(Bad_guy):
    def __init__(self,name:str,x:float,y:float,width:int,height:int,direction:str,frame_count:int,in_room:int,speed:list,sheet_size:list)->None:
        super().__init__(name,x,y,width,height,direction,frame_count,in_room,speed,sheet_size)

    def move(self,dt:float)->None:
        self.rect.x -=self.velocity.x *dt
        if self.rect.x < -128:
            self.rect.x = WIDTH + 30

    def update(self,dt):
        self.move(dt)
        self.handle_animations()
        
    def draw(self,screen:pygame.Surface)->None:
        screen.blit(self.image,self.rect)

       

import pygame
from .Bad_Guy_Base import Bad_guy

class Main_Boss(Bad_guy):
    def __init__(self,name:str,x:float,y:float,width:int,height:int,direction:str,frame_count:int,in_room:int,speed:list,sheet_size:list)->None:
        super().__init__(name,x,y,width,height,direction,frame_count,in_room,speed,sheet_size)
        self.got_turtle = False
    
    def get_turtle(self,jesse,dt):
        if pygame.sprite.collide_mask(self,jesse):
            self.got_turtle = True
        if self.got_turtle is True:
            self.rect.y += self.speed[1] *dt
        elif self.got_turtle is False:
            self.rect.y -= self.speed[1] * dt
    
    def update(self)->None:
        self.handle_animations()
        
    def update_cutscene(self,jesse,dt):
        self.get_turtle(jesse,dt)
        self.handle_animations()
    
    def draw(self,screen:pygame.Surface)->None:
        screen.blit(self.image,self.rect)

boss = Main_Boss("Boss",472,700,96,96,"Up",4,1,[150,150],[503,155])
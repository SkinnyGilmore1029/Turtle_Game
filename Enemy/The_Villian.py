import pygame
from .Bad_Guy_Base import Bad_guy
from The_turtles.The_player import player

class Main_Boss(Bad_guy):
    def __init__(self,name:str,x:float,y:float,width:int,height:int,direction:str,frame_count:int,in_room:int,speed:list,sheet_size:list)->None:
        super().__init__(name,x,y,width,height,direction,frame_count,in_room,speed,sheet_size)
        self.got_turtle = False
        self.starting_pos:tuple[int,int] = (self.x,self.y)
    
    def get_turtle(self,jesse,dt):
        if pygame.sprite.collide_mask(self,jesse):
            self.got_turtle = True
        if self.got_turtle is True:
            self.rect.y += self.speed[1] *dt
        elif self.got_turtle is False:
            self.rect.y -= self.speed[1] * dt
    
    def shut_level8(self,dt):
        if player.rect.x >= 350:
            self.rect.x -= (self.speed[0] * 2) *dt
            if self.rect.x <= 750:
                self.rect.x = 750
    
    def update(self,dt)->None:
        self.handle_animations()
        self.shut_level8(dt)
        
        
    def update_cutscene(self,jesse,dt):
        self.get_turtle(jesse,dt)
        self.handle_animations()
    
    def draw(self,screen:pygame.Surface)->None:
        screen.blit(self.image,self.rect)

boss = Main_Boss("Boss",472,700,96,96,"Up",4,1,[150,150],[503,155])
boss2 = Main_Boss("Boss",1000,400,96,96,"Up",4,1,[150,150],[503,155])
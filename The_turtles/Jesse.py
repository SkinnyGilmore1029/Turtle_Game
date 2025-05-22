import pygame
from .The_player import Player
from Utility.Settings import HEIGHT


class Jesse(Player):
    def __init__(self,name:str,x:float,y:float,width:int,height:int,direction:str,frame_count:int):
        super().__init__(name,x,y,width,height,direction,frame_count)
        self.scaled = False
        
    def getting_captured(self,player:object,boss:object,dt:float)->None:
        if not self.scaled:
            self.image = pygame.transform.smoothscale(self.image,(128,128)).convert_alpha()
            self.image.set_colorkey((255,255,255))
            self.mask = pygame.mask.from_surface(self.image)
            self.scaled = True
            
        if pygame.sprite.collide_mask(self,boss):
            self.rect.y += boss.speed[1] * dt
            self.direction = "Down"
            player.chase = True
        if self.rect.y >= HEIGHT:
            self.rect.y = HEIGHT
    
    
jesse = Jesse("Turtle2",472,210,64,64,"Up",6)

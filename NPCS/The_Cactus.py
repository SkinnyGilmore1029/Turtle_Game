import pygame
from .Npc_base import Animated_Npc_base
from Utility.Image_Handler import data
from The_turtles.The_player import player

class Cactus(Animated_Npc_base):
    def __init__(self, name:str, x:float, y:float,width:int, height:int,direction:str,frame_count:int,sheet_size:list)->None:
        super().__init__(name,x,y,width,height,direction,frame_count,sheet_size)
        self.touched = False
       
    def collision(self):
        pass
    
    def update(self):
        self.handle_animations()
        
    def draw(self,screen)->None:
        screen.blit(self.image,self.rect) 


class Cactus_Group(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
    
    def get_level_cactus(self,level:int,room:int)->None:
        self.empty()
        in_level = data.load_level_data(level,"Npc")["The_Cactus"]
        for c in in_level.values():
            if c["in_room"] == room:
                cactus = self.create_cactus(c)
                self.add(cactus)
                
    def create_cactus(self,data:dict)->Cactus:
        return Cactus(
            name= data['name'],
            x= data['x'],
            y= data['y'],
            width= data['width'],
            height= data['height'],
            direction= data['direction'],
            frame_count= data['frame_count'],
            sheet_size= data['sheet_size']
        )
        
    def update(self)->None:
        for sprite in self:
            sprite.update()
    
    def draw(self,screen)->None:
        for sprite in self:
            sprite.draw(screen)
            
All_cactus = Cactus_Group()
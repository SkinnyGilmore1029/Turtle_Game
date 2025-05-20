import pygame
from Utility.Image_Handler import data
from .Collectables import (
    Keys
)

class Collectable_Group(pygame.sprite.Group):
    collect_classes = {
        "Key" : Keys
    }
    def __init__(self):
        super().__init__()
        
    def get_level_keys(self,level:int,room:int)->None:
        level_data = data.load_level_Key_Lock_data(level)
        level_keys = level_data["Key"]
        if level_keys['in_room'] == room:
            key = self.create_collectable_from_data(level_keys)
            self.add(key)
                
    def create_collectable_from_data(self,data:dict):
        clas = self.collect_classes.get(data['name'])
        if clas:
            return clas(
                name= data['name'],
                x= data['x'],
                y= data['y'],
                width= data['width'],
                height= data['height']
            )
    
    def check_collected(self):
        for sprite in self:
            if sprite.collected == True :
                self.remove(sprite)
       
    def update(self,player):
        for sprite in self:
            sprite.update(player)
        self.check_collected()
            
    def draw(self,screen:pygame.Surface):
        for sprite in self:
            sprite.draw(screen)
            
Collect_group = Collectable_Group()
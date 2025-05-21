import pygame
from Utility.Image_Handler import data
from .Collectables import (
    Keys,
    OneUps
)

class Collectable_Group(pygame.sprite.Group):
    collect_classes = {
        "Key" : Keys,
        "1up" : OneUps
    }
    def __init__(self):
        super().__init__()
        self.already_in_level = set()
        self.already_collected = set()
        
    def get_level_keys(self,level:int,room:int)->None:
        set_key = ("key",level,room)
        if set_key not in self.already_in_level:
            level_data = data.load_level_Key_Lock_data(level)
            level_keys = level_data["Key"]
            if level_keys['in_room'] == room:
                collected_key = (level_keys['collected key'])
                if collected_key not in self.already_collected:
                    key = self.create_collectable_from_data(level_keys)
                    self.add(key)
            self.already_in_level.add(set_key)

    
    def get_level_OneUps(self,level:int,room:int)->None:
        set_key = ("Oneup",level,room)
        if set_key not in self.already_in_level:
            oneup_data = data.load_level_collectables_data(level)
            for up in oneup_data.values():
                if up['in_room'] == room:
                    collected_key = (up['collected key'])
                    if collected_key not in self.already_collected:
                        oneup = self.create_collectable_from_data(up)
                        self.add(oneup)
            self.already_in_level.add(set_key)
            
    def get_level_collectables(self,level:int,room:int)->None:
        self.empty()
        self.already_in_level.clear()
        self.get_level_keys(level,room)
        self.get_level_OneUps(level,room)

    def create_collectable_from_data(self,data:dict):
        clas = self.collect_classes.get(data['name'])
        if clas:
            return clas(
                name= data['name'],
                x= data['x'],
                y= data['y'],
                width= data['width'],
                height= data['height'],
                collected_key= data['collected key']
            )
    
    def check_collected(self):
        for sprite in self:
            if sprite.collected == True :
                self.already_collected.add((sprite.collected_key))
                self.remove(sprite)
       
    def update(self,player):
        for sprite in self:
            sprite.update(player)
        self.check_collected()
            
    def draw(self,screen:pygame.Surface):
        for sprite in self:
            sprite.draw(screen)
            
Collect_group = Collectable_Group()
import pygame
from Utility.Image_Handler import data
from .Locks import Lock

class Lock_Group(pygame.sprite.GroupSingle):
    def __init__(self):
        super().__init__()
        
    def get_level_lock(self,level:int,room:int)->None:
        self.empty()
        lock_data = data.load_level_Key_Lock_data(level)
        level_lock = lock_data["Lock"]
        if level_lock["in_room"] == room:
            lock = self.create_lock_from_data(level_lock)
            self.add(lock)
            
    def create_lock_from_data(self,data:dict):
        return Lock(
            name= data["name"],
            x= data['x'],
            y= data['y'],
            width= data['width'],
            height= data['height']
        )
    
    def check_locked(self):
        if self.sprite:
            if self.sprite.locked == False:
                self.remove(self.sprite)
            
    def update(self,player)->None:
        if self.sprite:
            self.sprite.update(player)
        self.check_locked()
        
    def draw(self,screen)->None:
        if self.sprite:
            self.sprite.draw(screen)
        
        
the_lock = Lock_Group()
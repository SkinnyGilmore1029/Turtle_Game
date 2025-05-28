import pygame
from Utility.Image_Handler import data
from .Locks import Lock

class Lock_Group(pygame.sprite.GroupSingle):
    def __init__(self):
        super().__init__()
        self.already_unlocked = set()
        
    def get_level_lock(self,level:int,room:int)->None:
        self.empty()
        lock_data = data.load_level_data(level,"Lock_Key")
        level_lock = lock_data["Lock"]
        if level_lock["in_room"] == room:
            unlocked_key = (level_lock['name'],level_lock['x'],level_lock['y'])
            if unlocked_key not in self.already_unlocked:
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
                self.already_unlocked.add((self.sprite.name,self.sprite.x,self.sprite.y))
                self.remove(self.sprite)
            
    def update(self,player)->None:
        if self.sprite:
            self.sprite.update(player)
        self.check_locked()
        
    def draw(self,screen)->None:
        if self.sprite:
            self.sprite.draw(screen)
    
    def clear_level(self):
        self.empty()
        self.already_unlocked.clear()
        
the_lock = Lock_Group()
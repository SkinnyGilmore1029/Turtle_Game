import pygame
from Utility.Image_Handler import data
from .The_Enemies import (
    The_cars,
    The_trucks,
    The_bus,
    The_gators
)

class The_Bad_Guys(pygame.sprite.Group):
    badguy_classes = {
            "Car" : The_cars,
            "Truck" : The_trucks,
            "Bus" : The_bus,
            "Gator" : The_gators
        }
    def __init__(self):
        super().__init__()
        
    def get_level_badguys(self,level:int,room:int):
        self.empty()
        in_level = data.load_level_enemies_data(level) #should be dict full of enemis
        for m in in_level.values():
            if m['in_room'] == room:
                badguy = self.create_badguy_from_data(m)
                self.add(badguy)
        
    def create_badguy_from_data(self,data:dict):
        clas = self.badguy_classes.get(data["name"])
        if clas:
            return clas(
                name= data["name"],
                x= data['x'],
                y= data["y"],
                width= data["width"],
                height= data["height"],
                direction= data["direction"],
                frame_count= data["frame_count"],
                in_room= data["in_room"]
            )

    def collision_with_player(self,player)->None:
        for sprite in self:
            if pygame.sprite.collide_mask(sprite,player):
                return True
        return False

    def update(self,dt:float):
        for sprite in self:
            sprite.update(dt)
            
    def draw(self,screen:pygame.Surface):
        for sprite in self:
            sprite.draw(screen)

bad_guys = The_Bad_Guys()
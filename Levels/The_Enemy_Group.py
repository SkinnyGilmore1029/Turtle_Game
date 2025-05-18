import pygame
from Utility.Image_Handler import load_enemy_in_room
from .The_Enemies import (
    The_cars,
    The_trucks,
    The_bus
)

class The_Bad_Guys(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        
    def get_level_badguys(self,level:int,room:int):
        self.empty()
        in_level = load_enemy_in_room(level) #should be dict full of enemis
        for m in in_level.values():
            if m['in_room'] == room:
                badguy = self.create_badguy_from_data(m)
                self.add(badguy)
        
    def create_badguy_from_data(self,data:dict):
        match data["name"]:
            case "Car":
                return The_cars(
                                name= data["name"],
                                x= data['x'],
                                y= data["y"],
                                width= data["width"],
                                height= data["height"],
                                direction= data["direction"],
                                frame_count= data["frame_count"],
                                in_room= data["in_room"]
                            )
            case "Truck":
                return The_trucks(
                    name=data["name"],
                    x=data["x"],
                    y=data["y"],
                    width=data["width"],
                    height=data["height"],
                    direction=data["direction"],
                    frame_count=data["frame_count"],
                    in_room=data["in_room"]
                )
            case "Bus":
                return The_bus(
                    name=data["name"],
                    x=data["x"],
                    y=data["y"],
                    width=data["width"],
                    height=data["height"],
                    direction=data["direction"],
                    frame_count=data["frame_count"],
                    in_room=data["in_room"]
                )

    def update(self,dt:float):
        for sprite in self:
            sprite.update(dt)
            
    def draw(self,screen:pygame.Surface):
        for sprite in self:
            sprite.draw(screen)

bad_guys = The_Bad_Guys()
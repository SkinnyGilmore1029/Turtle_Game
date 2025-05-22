import pygame
from Utility.Image_Handler import data

class Screens:
    def __init__(self,name:str):
        self.name = name
        self.fonts:dict = {
            "Title" : pygame.font.SysFont("Arial",48,True),
            "Start Button" : pygame.font.SysFont("Arial",32,True)
        }

    def change_scene(self,new_name:str)->None:
        self.name = new_name
        self.background = data.load_image(new_name)
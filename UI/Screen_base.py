import pygame

class Screens:
    def __init__(self,name:str):
        self.name = name
        self.fonts:dict = {
            "Title" : pygame.font.SysFont("Arial",48,True),
            "Start Button" : pygame.font.SysFont("Arial",32,True)
        }


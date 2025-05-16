import pygame
from Utility.Settings import WIDTH,HEIGHT
from Utility.Image_Handler import load_level_background

class Level_Backgrounds:
    def __init__(self,level_num:int,room_num:int)->None:
        self.level_num = level_num
        self.room_num = room_num
        self.image = load_level_background(self.level_num,self.room_num)
        self.rect = self.image.get_frect()
        
    def draw(self,screen):
        screen.blit(self.image,self.rect)
        

import pygame
from Utility.Settings import WIDTH,HEIGHT
from Utility.Image_Handler import data

class Level_Backgrounds:
    def __init__(self,level_num:int,room_num:int)->None:
        self.level_num = level_num
        self.room_num = room_num
        self.image = data.load_background_image(self.level_num,self.room_num)
        self.rect = self.image.get_frect()
        self.room_list = []
        
    def draw(self,screen):
        screen.blit(self.image,self.rect)

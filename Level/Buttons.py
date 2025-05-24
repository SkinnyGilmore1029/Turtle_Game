import pygame
from Utility.Image_Handler import data
from The_turtles.The_player import player

class Button(pygame.sprite.Sprite):
    def __init__(self,x:float, y:float, width:int, height:int):
        super().__init__()
        self.name = "Red Star"
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        self.image = data.load_image(self.name)
        self.rect = pygame.FRect(self.x,self.y,self.w,self.h)
        self.mask = pygame.mask.from_surface(self.image)
        self.pressed = False
    
    def getting_pressed(self):
        if pygame.sprite.collide_mask(self,player):
            self.pressed = True
            return True
        return False
    
    def update(self):
        if self.pressed is True:
            self.name = "Green Star"
        
    def draw(self,screen:pygame.Surface)->None:
        screen.blit(self.image,self.rect)
        
class The_Buttons(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.already_in_level = set()
        self.already_collected = set()
        
    
        
    
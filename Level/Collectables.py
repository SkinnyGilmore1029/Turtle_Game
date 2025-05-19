import pygame
from Utility.Image_Handler import data

class Collectable(pygame.sprite.Sprite):
    def __init__(self,name:str, x:float, y:float,width:int,height:int):
        super().__init__()
        self.name = name
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        self.image = data.load_image(name)
        self.image = pygame.transform.smoothscale(self.image,(self.w,self.h))
        self.rect = pygame.FRect(self.x,self.y,self.w,self.h)
        self.mask = pygame.mask.from_surface(self.image)
        self.collected = False
        self.used = False
        self.can_give = False
        
    def collect(self,player:object)->None:
        if pygame.sprite.collide_mask(self,player):
            self.collected = True
            self.can_give = True
            
class Keys(Collectable):
    def __init__(self,name:str,x:float,y:float,width:int,height:int):
        super().__init__(name,x,y,width,height)
        
    def draw(self,screen:pygame.Surface)->None:
        screen.blit(self.image,self.rect)
        
key1 = Keys("Key",300,300,32,32)
import pygame
from Utility.Image_Handler import data



class Npc_Base(pygame.sprite.Sprite):
    def __init__(self,name:str,x:float,y:float,width:float,height:float)->None:
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
        self.font = pygame.font.SysFont("Arial",24,True)
        
    def upadat(self):
        #update will be filled in with childern class methods
        pass
    
    def draw(self,screen:pygame.Surface)->None:
        screen.blit(self.image,self.rect)
        

            
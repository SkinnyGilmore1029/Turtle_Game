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
        
    def collect(self,player)->None:
        pass
    
    def get_collected(self,player)->None:
        if pygame.sprite.collide_mask(self,player):
            self.collect(player)
    
    def update(self,player)->None:
        self.get_collected(player)
    
    def draw(self,screen:pygame.Surface)->None:
        screen.blit(self.image,self.rect)
            
class Keys(Collectable):
    def __init__(self,name:str,x:float,y:float,width:int,height:int):
        super().__init__(name,x,y,width,height)
    
    
    def collect(self,player)->None:
        self.collected = True
        player.key_count +=1
        print("collected")


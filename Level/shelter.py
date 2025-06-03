import pygame
from Utility.Image_Handler import data
from Enemy.The_Enemy_Group import bad_guys

class Shelters(pygame.sprite.Sprite):
    def __init__(self,name:str,x:float,y:float,width:int,height:int):
        super().__init__()
        self.name = name
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        self.image = data.load_image(self.name)
        self.image = pygame.transform.smoothscale(self.image,(self.w,self.h))
        self.rect = pygame.FRect(self.x,self.y,self.w,self.h)
        self.mask = pygame.mask.from_surface(self.image)
    
    def tornado_colission(self):
        for e in bad_guys:
            if pygame.sprite.collide_mask(self,e):
                e.speed[0] *= -1
                e.speed[1] *= -1
       
    def update(self):
        self.tornado_colission()
    
    def draw(self,screen)->None:
        screen.blit(self.image,self.rect)
    
class Shelter_group(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        
    def get_shelter_data(self,level_num:int,room:int):
        self.empty()
        shelter_data = data.load_level_data(level_num,"shelter")
        for s in shelter_data.values():
            if s['in_room'] == room:
                shelter = self.create_shelter(s)
                self.add(shelter)
            
    def create_shelter(self,data:dict)->Shelters:
        return Shelters (
            name= data["name"],
            x= data['x'],
            y= data['y'],
            width= data['width'],
            height= data['height']
        )
        
    def update(self):
        for sprite in self:
            sprite.update()
            
    def change_level(self):
        self.empty()
    
    def draw(self,screen)->None:
        for sprite in self:
            sprite.draw(screen)
            
The_shelters = Shelter_group()
        
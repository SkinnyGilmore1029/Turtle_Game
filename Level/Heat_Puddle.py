import pygame
from Utility.Image_Handler import data
from Utility.Settings import WIDTH
from The_turtles.The_player import player

class HeatBar:
    def __init__(self,x:int,y:int,w:int,h:int,max_hp:int) ->None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hp = max_hp
        self.max_hp = max_hp
        self.lose_hp = .25
        
    def draw(self,screen: pygame.Surface) -> None:
        ratio = self.hp/self.max_hp
        pygame.draw.rect(screen,"red",(self.x,self.y,self.w,self.h))
        pygame.draw.rect(screen,"green",(self.x,self.y,self.w*ratio, self.h))
        self.hp -=self.lose_hp  
        if self.hp <=0:
            player.lives -=1 
            player.rect.y = 0
            player.rect.x = WIDTH*.9
            self.hp=self.max_hp    
            
heat_bar = HeatBar(WIDTH//3,0,175,32,175)

class Puddles(pygame.sprite.Sprite):
    def __init__(self,name:str,x:int,y:int,width:int,height:int):
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
    
    def in_puddle(self) -> None:
            soaked = pygame.sprite.collide_mask(self,player)
            if soaked:
                heat_bar.hp +=1
                if heat_bar.hp >= heat_bar.max_hp:
                    heat_bar.hp = heat_bar.max_hp
    
    
    def update(self):
        self.in_puddle()
    
    def draw(self,screen: pygame.Surface) -> pygame.Surface:
        screen.blit(self.image,self.rect)

        
class The_Puddles(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        
    def get_puddle_data(self,level:int,room:int)->None:
        self.empty()
        puddles_data = data.load_level_data(level,"puddles")
        for p in puddles_data.values():
            if p["in_room"] == room:
                puddle = self.create_puddle(p)
                self.add(puddle)
                
    def create_puddle(self,data:dict)->Puddles:
        return Puddles(
            name= data["name"],
            x= data['x'],
            y= data['y'],
            width= data['width'],
            height= data['height']
        )
        
    def update(self):
        for sprite in self:
            sprite.update()
        
    def draw(self,screen:pygame.Surface)->None:
        for sprite in self:
            sprite.draw(screen)
        
All_puddles = The_Puddles()
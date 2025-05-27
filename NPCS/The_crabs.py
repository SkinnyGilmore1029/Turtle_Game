import pygame
from .Npc_base import Npc_Base
from The_turtles.The_player import player
from Utility.Settings import HEIGHT , WIDTH
from Utility.Image_Handler import data


class Crabby(Npc_Base):
    def __init__(self,name:str,x:float,y:float,width:int,height:int,direction:str,name2:str):
        super().__init__(name,x,y,width,height)
        self.go_down:bool = False
        self.cross_screen:bool = False
        self.despawn:bool = False
        self.speed:tuple[int,int] = (350,150)
        self.direction = direction
        self.name2 = name2
        self.rotate_crabs()
    
    def rotate_crabs(self):
        match self.direction:
            case "Up":
                self.imgae = pygame.transform.flip(self.image,False,False)
                self.mask = pygame.mask.from_surface(self.image)
            case "Down":
                self.imgae = pygame.transform.flip(self.image,False,True)
                self.mask = pygame.mask.from_surface(self.image)
    
    def get_pushed(self):
        if pygame.sprite.collide_mask(self,player):
            self.go_down = True
        
    def move_down(self,dt:float):
        if self.go_down == True:
            match self.direction:
                case "Up":
                    #crab on the bottum
                    self.rect.y += self.speed[1] * dt
                    if self.rect.top >= HEIGHT:
                        self.go_down = False
                        self.cross_screen = True
                        self.direction = "Left" #move left from the right
                        self.rect.y = HEIGHT*.3
                        self.rect.x = WIDTH -self.w  
                        
                case "Down":
                    #crab on top
                    self.rect.y -= self.speed[1] * dt
                    if self.rect.bottom <= 0:
                        self.go_down = False
                        self.cross_screen = True
                        self.direction = "Right" #move right from the left
                        self.rect.x = -96
                        self.rect.y = HEIGHT *.7

    
    def moving_across(self,dt:float):
        if self.cross_screen == True:
            match self.direction :
                case "Left":
                    self.rect.x -= self.speed[0] * dt
                    if self.rect.x < -96:
                        self.rect.x = -96
                        self.despawn = True
                case "Right":
                    self.rect.x += self.speed[0] * dt
                    if self.rect.x > WIDTH:
                        self.rect.x = WIDTH
                        self.despawn = True
                        
    def update(self,dt:float):
        self.get_pushed()
        self.move_down(dt)
        self.moving_across(dt)
        
    def draw(self,screen:pygame.Surface)->None:
        screen.blit(self.image,self.rect)

class The_crabbies(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.already_in_level = set()
        self.already_pushed = set()
        
    def get_level_crabs(self,level:int,room:int)->None:
        self.empty()
        in_level = data.load_level_data(level,"Npc")["Crabs"]
        for c in in_level.values():
            if c["in_room"] == room and c['name2'] not in self.already_pushed:
                crab = self.create_crab(c)
                self.add(crab)
                
    def create_crab(self,data:dict)->None:
        return Crabby(
            name= data["name"],
            x= data['x'],
            y= data["y"],
            width= data["width"],
            height= data["height"],
            direction= data["direction"],
            name2= data["name2"]
        )

    def check_despawn(self):
        for sprite in self:
            if sprite.despawn == True:
                self.already_pushed.add(sprite.name2)
                self.remove(sprite)
                
    
    def clear_level(self):
        self.empty()
        self.already_pushed.clear()
        self.already_pushed.clear()
    
    def update(self,dt:float)->None:
        for sprite in self:
            sprite.update(dt)
        self.check_despawn()
            
    def draw(self,screen:pygame.Surface)->None:
        for sprite in self:
            sprite.draw(screen)
            
The_Crabs = The_crabbies()
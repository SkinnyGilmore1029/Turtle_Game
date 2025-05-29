import pygame
from .Npc_base import Animated_Npc_base
from Utility.Image_Handler import data
from The_turtles.The_player import player
from .The_Cactus import All_cactus
from .The_Lizard import Lizards

class Fly(Animated_Npc_base):
    def __init__(self, name:str, x:float, y:float,width:int, height:int,direction:str,frame_count:int,sheet_size:list,
                 speed:list,home_cactus:object)->None:
        super().__init__(name,x,y,width,height,direction,frame_count,sheet_size)
        self.come_off_cactus = False
        self.collected = False
        self.speed:list = speed
        self.velocity = pygame.Vector2(self.speed[0],self.speed[1])
        self.home_cactus = home_cactus
    
    def fly_around(self,dt)->None:
        if self.collected == False:
            self.rect.y -= self.velocity.y *dt
            self.rect.x -= self.velocity.x *dt
    
    def collision_with_player(self):
        if pygame.sprite.collide_mask(self,player):
            if self.collected == False:
                Lizards.flies_collected +=1
                print(Lizards.flies_collected)
                self.collected = True
                
                
        
    def collision_with_cactus(self):
        c = self.home_cactus
        if pygame.sprite.collide_mask(self,c):
            if self.rect.top < c.rect.top:
                self.rect.bottom = c.rect.top
                self.velocity.y *=-1
            elif self.rect.bottom > c.rect.bottom:
                self.rect.top = c.rect.bottom
                self.velocity.y *=-1
            elif self.rect.right < c.rect.right:
                self.rect.right = c.rect.left
                self.velocity.x *=-1
            elif self.rect.left > c.rect.left:
                self.rect.left = c.rect.right
                self.velocity.x *=-1
    
    def update(self,dt):
        self.collision_with_cactus()
        self.collision_with_player()
        self.fly_around(dt)
        self.handle_animations()
        
    def draw(self,screen)->None:
        screen.blit(self.image,self.rect) 
        
class Fly_Group(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.all_flies = []
    
    def get_level_flies(self, level:int, room:int)->None:
        self.empty()
        in_level = data.load_level_data(level,"Npc")["The_Flies"]
        flies_data = list(in_level.values())
        
        for fly_data, cactus in zip(flies_data, All_cactus):
            if fly_data["in_room"] == room:
                the_fly = self.create_fly(fly_data, cactus)
                self.all_flies.append(the_fly)
    
    def check_edges(self):
        for sprite in self:
            c = sprite.home_cactus
            if sprite.rect.y >= c.rect.y + 150 or sprite.rect.y <= c.rect.y - 110 or sprite.rect.y <= 75:
                sprite.velocity.y *= -1
            if sprite.rect.x >= c.rect.x + 100 or sprite.rect.x <= c.rect.x - 100:
                sprite.velocity.x *= -1

                    
    def create_fly(self,data:dict,cactus:object)->Fly:
        return Fly(
            name= data['name'],
            x= data['x'],
            y= data['y'],
            width= data['width'],
            height= data['height'],
            direction= data['direction'],
            frame_count= data['frame_count'],
            sheet_size= data['sheet_size'],
            speed = data['speed'],
            home_cactus= cactus
        )
        
    def update(self,dt)->None:
        for fly in self.all_flies:
            if fly.home_cactus.touched and fly not in self and not fly.collected:
                self.add(fly)
            if fly.collected:
                self.remove(fly)
        for sprite in self:
            sprite.update(dt)
        self.check_edges()
    
    def draw(self,screen)->None:
        for sprite in self:
            sprite.draw(screen)
            
All_Flies = Fly_Group()
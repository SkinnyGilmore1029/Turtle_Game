import pygame
from Utility.Image_Handler import data
from Utility.Settings import HEIGHT
from The_turtles.The_player import player


class Lily_Pad(pygame.sprite.Sprite):
    def __init__(self,name:str,x:float,y:float,width:int,height:int,direction)->None:
        super().__init__()
        self.name = name
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        self.image = data.load_image(self.name)
        self.imgae = pygame.transform.smoothscale(self.image,(self.w,self.h))
        self.rect = pygame.FRect(self.x,self.y,self.w,self.h)
        self.mask = pygame.mask.from_surface(self.image)
        self.direction = direction
        self.speed = 200

    
    def move_lily(self,dt):
        match self.direction:
            case "Up":
                self.rect.y += self.speed *dt
                if self.rect.y > HEIGHT:
                    self.rect.y = 0
            case "Down":
                self.rect.y -= self.speed *dt
                if self.rect.y < 0:
                    self.rect.y = HEIGHT
    
    def transport(self,dt):
        if pygame.sprite.collide_mask(self,player):
            match self.direction:
                case "Up":
                    player.rect.y -= 200 *dt
                case "Down":
                    player.rect.y += 200 *dt
                    
    def update(self,dt:float):
        self.move_lily(dt)
        self.transport(dt)
        
    def draw(self,screen:pygame.Surface)->None:
        screen.blit(self.image,self.rect)
        
class The_Lily_Pads(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.loaded_room = set()
        
    def get_lily_data(self,level:int,room:int)->None:
        key = (level,room)
        if key not in self.loaded_room:
            lily_data = data.load_level_data(level,"Lily_Pads")
            for l in lily_data.values():
                if l['room'] == room:
                    lily_pad = self.create_lilies(l)
                    self.add(lily_pad)
            self.loaded_room.add(key)
            
    def create_lilies(self,data:dict)->Lily_Pad:
        return Lily_Pad(
            name= data["name"],
            x= data['x'],
            y= data['y'],
            width= data['width'],
            height= data['height'],
            direction= data['direction']
        )
        
    def update(self,dt:float)->None:
        for sprite in list(self):
            sprite.update(dt)
    
    def change_room(self):
        self.empty()
        self.loaded_room.clear()
    
    def draw(self,screen:pygame.Surface)->None:
        for sprite in self:
            sprite.draw(screen)
    
All_Lily = The_Lily_Pads()
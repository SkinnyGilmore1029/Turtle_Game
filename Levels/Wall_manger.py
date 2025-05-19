import pygame
from Utility.Image_Handler import data

class The_Walls(pygame.sprite.Sprite):
    def __init__(self,name:str,x:float,y:float,width:float,height:float,direction:str,room:int)->None:
        super().__init__()
        self.image = data.load_image(name)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.room = room
        self.direction = direction
        self.handle_wall_direction()
        self.rect = pygame.FRect(self.x,self.y,self.width,self.height)
        self.mask = pygame.mask.from_surface(self.image)

    def handle_wall_direction(self):
        match self.direction:
            case "top":
                self.image = pygame.transform.smoothscale(self.image,(self.width,self.height))
            case "bottom":
                self.image = pygame.transform.smoothscale(self.image,(self.width,self.height))
                self.image = pygame.transform.flip(self.image,False,True)
            case "left":
                self.image = pygame.transform.rotate(self.image, -90.0)
                self.image = pygame.transform.flip(self.image, True, False)
                self.image = pygame.transform.smoothscale(self.image, (self.width, self.height))
            case 'right':
                self.image = pygame.transform.rotate(self.image, -90.0)
                self.image = pygame.transform.smoothscale(self.image, (self.width, self.height))
        self.mask = pygame.mask.from_surface(self.image)

    def wall_collision(self,josh) -> None:
        if pygame.sprite.collide_mask(self,josh):
            if josh.rect.top <= self.rect.top:
                josh.rect.bottom = self.rect.top
            elif josh.rect.bottom >= self.rect.bottom:
                josh.rect.top = self.rect.bottom
            elif josh.rect.right < self.rect.right:
                josh.rect.right = self.rect.left
            elif josh.rect.left > self.rect.left:
                josh.rect.left = self.rect.right

    def draw(self,screen,josh):
        self.wall_collision(josh)
        screen.blit(self.image,self.rect)
        
class The_walls_group(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.loaded_room = set()
        
        
    def load_group(self,level:int,room:int)->None:
        key = (level,room)
        if key not in self.loaded_room:
            walls = data.load_wall_data(level)
            for w in walls.values():
                if w['room'] == room:
                    wall = The_Walls(name= w.get("name","Fence"),
                                    x= w.get("x",0),
                                    y= w.get("y",0),
                                    width= w.get("width",128),
                                    height= w.get("height",128),
                                    direction= w.get("direction","up"),
                                    room= w.get("room",1))
                    self.add(wall)
            self.loaded_room.add(key)
    
    def change_level(self):
        self.empty()
        self.loaded_room.clear()
        
    
    def draw(self,screen:pygame.Surface,josh)->None:
        for sprite in self:
            sprite.draw(screen,josh)
            
All_walls = The_walls_group()
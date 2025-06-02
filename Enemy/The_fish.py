import pygame
from Utility.Settings import HEIGHT
from Utility.Image_Handler import data


class The_Fish(pygame.sprite.Sprite):
    def __init__(self,name:str,x:float,y:float,width:int,height:int,direction:str,frame_count:int,in_room:int,speed:list,sheet_size:list)->None:
        super().__init__()
        self.name = name
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        self.direction = direction
        self.frame_count = frame_count
        self.in_room = in_room
        self.speed = speed
        self.velocity = pygame.Vector2(speed[0],speed[1])
        self.sheet_size = sheet_size
        self.image = data.load_image(self.name)
        self.handle_direction()
        self.rect = pygame.FRect(self.x,self.y,self.w,self.h)
        self.mask = pygame.mask.from_surface(self.image)

    def handle_direction(self):
        self.image = pygame.transform.smoothscale(self.image,(self.w,self.h))
        match self.direction:
            case "Up":
                self.image = pygame.transform.rotate(self.image,-90.0)
                self.mask = pygame.mask.from_surface(self.image)
            case "Down":
                self.image = pygame.transform.rotate(self.image,90.0)
                self.mask = pygame.mask.from_surface(self.image)

    def move(self,dt:float)->None:
        self.rect.y += self.velocity.y *dt
        match self.direction:
            case "Up":
                if self.rect.y < -160:
                    self.rect.y = HEIGHT -160
            case "Down":
                if self.rect.y > HEIGHT - 160:
                    self.rect.y = -160
    
    def update(self,dt:float)->None:
        self.move(dt)
        
        
    def draw(self,screen:pygame.Surface)->None:
        screen.blit(self.image,self.rect)
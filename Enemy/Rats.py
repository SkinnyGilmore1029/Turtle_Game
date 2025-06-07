import pygame
from Utility.Image_Handler import data


class The_Rats(pygame.sprite.Sprite):
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
        self.rect = pygame.FRect(self.x,self.y,self.w,self.h)
        self.mask = pygame.mask.from_surface(self.image)
        self.start_pos = (x,y)
        
        
    def turn_rat_side(self):
        if self.direction == "Left":
            self.image = pygame.transform.rotate(self.image,-90)
            self.image = pygame.transform.flip(self.image,True,False)
        elif self.direction == "Right":
            self.image = pygame.transform.rotate(self.image,-90)
    
    def move(self,dt):
        self.rect.y += self.velocity.y *dt
        self.rect.x += self.velocity.x *dt
    
    def update(self,dt)->None:
        self.move(dt)
        
    def draw(self,screen:pygame.Surface)->None:
        screen.blit(self.image,self.rect)
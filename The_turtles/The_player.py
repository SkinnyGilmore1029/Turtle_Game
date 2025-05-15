import pygame
from Utility.Settings import WIDTH,HEIGHT
from Utility.Image_Handler import load_image

class Player(pygame.sprite.Sprite):
    def __init__(self, name:str, x:float, y:float,width:int, height:int):
        super().__init__()
        self.name = name
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        self.image = load_image(self.name)
        self.rect = pygame.FRect(self.x,self.y,self.w,self.h)
        self.direction = "Up"
        self.direction_facing()
        self.mask = pygame.mask.from_surface(self.image)
        self.velocity = pygame.Vector2(0,0)

    def direction_facing(self)->None:
        match self.direction:
            case "Up":
                self.image = pygame.transform.smoothscale(self.image,(self.w,self.h))
            case "Down":
                self.image = pygame.transform.smoothscale(self.image,(self.width,self.height))
                self.image = pygame.transform.flip(self.image,False,True)
            case "Left":
                self.image = pygame.transform.rotate(self.image, -90.0)
                self.image = pygame.transform.flip(self.image, True, False)
                self.image = pygame.transform.smoothscale(self.image, (self.width, self.height))
            case "Right":
                self.image = pygame.transform.rotate(self.image, -90.0)
                self.image = pygame.transform.smoothscale(self.image, (self.width, self.height))
        self.mask = pygame.mask.from_surface(self.image)
        
    def move(self,dt:float)->None:
        keys = pygame.key.get_pressed()
        self.velocity.x = 0
        self.velocity.y = 0

        if keys[pygame.K_LEFT]:
            self.velocity.x = -100  # 100 pixels per second
        if keys[pygame.K_RIGHT]:
            self.velocity.x = 100
        if keys[pygame.K_UP]:
            self.velocity.y = -100
        if keys[pygame.K_DOWN]:
            self.velocity.y = 100

        # Apply movement using dt and velocity
        self.rect.x += self.velocity.x * dt
        self.rect.y += self.velocity.y * dt
        
    def draw(self,screen:pygame.Surface,dt:float)->None:
        self.move(dt)
        screen.blit(self.image,self.rect)
        
player = Player("Turtle",200,200,64,64)
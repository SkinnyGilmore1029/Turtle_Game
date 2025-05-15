import pygame
from Utility.Settings import WIDTH,HEIGHT
from Utility.Image_Handler import load_image

class Player(pygame.sprite.Sprite):
    def __init__(self, name:str, x:float, y:float,width:int, height:int,direction:str):
        super().__init__()
        self.name = name
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        self.image = None
        self.rect = pygame.FRect(self.x,self.y,self.w,self.h)
        self.direction = direction
        self.direction_facing()
        self.mask = pygame.mask.from_surface(self.image)
        self.velocity = pygame.Vector2(0,0)

    def direction_facing(self)->None:
        match self.direction:
            case "Up":
                self.image = pygame.transform.smoothscale(load_image(self.name),(self.w,self.h))
            case "Down":
                self.image = pygame.transform.smoothscale(load_image(self.name),(self.width,self.height))
                self.image = pygame.transform.flip(load_image(self.name),False,True)
            case "Left":
                self.image = pygame.transform.rotate(load_image(self.name), -90.0)
                self.image = pygame.transform.flip(load_image(self.name), True, False)
                self.image = pygame.transform.smoothscale(load_image(self.name), (self.width, self.height))
            case "Right":
                self.image = pygame.transform.rotate(load_image(self.name), -90.0)
                self.image = pygame.transform.smoothscale(load_image(self.name), (self.width, self.height))
        self.mask = pygame.mask.from_surface(self.image)
        
    def move(self,dt:float)->None:
        keys = pygame.key.get_pressed()
        self.velocity.x = 0
        self.velocity.y = 0

        if keys[pygame.K_LEFT]:
            self.velocity.x = -300  # 100 pixels per second
            self.direction = "Left"
        if keys[pygame.K_RIGHT]:
            self.velocity.x = 300
            self.direction = "Right"
        if keys[pygame.K_UP]:
            self.velocity.y = -300
            self.direction = "Up"
        if keys[pygame.K_DOWN]:
            self.velocity.y = 300
            self.direction = "Down"

        # Apply movement using dt and velocity
        self.rect.x += self.velocity.x * dt
        self.rect.y += self.velocity.y * dt
        
    def draw(self,screen:pygame.Surface,dt:float)->None:
        self.move(dt)
        screen.blit(self.image,self.rect)
        
player = Player("Turtle",200,200,64,64,"Up")
import pygame
from Utility.Settings import WIDTH
from .Bad_Guy_Base import Bad_guy


class The_gators(Bad_guy):
    def __init__(self,name:str,x:float,y:float,width:int,height:int,direction:str,frame_count:int,in_room:int,speed:list,sheet_size:list)->None:
        super().__init__(name,x,y,width,height,direction,frame_count,in_room,speed,sheet_size)
    
    def move_up_down(self, dt: float) -> None:
        self.rect.y += self.velocity.y * dt

        if self.rect.y <= 170:
            self.rect.y = 170
            self.velocity.y *= -1

        elif self.rect.y >= 480:
            self.rect.y = 480
            self.velocity.y *= -1
    
    def move_left_right(self, dt: float) -> None:
        self.rect.x += self.velocity.x * dt

        if self.rect.x <= 0:
            self.rect.x = 0
            self.velocity.x *= -1
            match self.direction:
                case "Left":
                    self.direction = "Right"
                case "Right":
                    self.direction = "Left"

        elif self.rect.x >= WIDTH - self.w:
            self.rect.x = WIDTH - self.w
            self.velocity.x *= -1
            match self.direction:
                case "Left":
                    self.direction = "Right"
                case "Right":
                    self.direction = "Left"

    def move(self,dt:float)->None:
        self.move_left_right(dt)
        self.move_up_down(dt)
    
    def update(self,dt:float)->None:
        self.move(dt)
        self.handle_animations()
        
    def draw(self,screen:pygame.Surface)->None:
        screen.blit(self.image,self.rect)
from Utility.Settings import HEIGHT
from .Bad_Guy_Base import Bad_guy
from .The_Villian import boss2
from Level.Buttons import Button_group
import pygame

class The_Bolders(Bad_guy):
    def __init__(self,name:str,x:float,y:float,width:int,height:int,direction:str,frame_count:int,in_room:int,speed:list,sheet_size:list)->None:
        super().__init__(name,x,y,width,height,direction,frame_count,in_room,speed,sheet_size)
        self.start_pos = (x,y)
        self.final_spawn = False
    
    
    def final_bolder(self):
        buttons_needed = ["Button1 l8","Button3 l8"]
        for button in Button_group:
            if button.name2 in buttons_needed and button.pressed:
                self.final_spawn = True

    def move_final_bolder(self,dt):
        if self.final_spawn:
            self.rect.x += (self.speed[0] * 2) * dt
            if self.rect.x >= 1200:
                self.rect.x = 1200
                self.speed[0] = 0
    
    def smash_door(self,wall,dt):
        if pygame.sprite.collide_mask(self,wall):
            wall.rect.x += (self.speed[0] * 2) * dt
            if wall.rect.x >= 1200:
                wall.rect.x = 1200
                
                
    
    def smash_villian(self):
        if pygame.sprite.collide_mask(self,boss2):
            boss2.rect.x = 1200
            boss2.rect.y = 0
            
                
    def final_update(self,wall,dt):
        self.final_bolder()
        if self.final_spawn:
            self.move_final_bolder(dt)
            self.smash_door(wall,dt)
            self.smash_villian()
        
    def draw_final(self,screen):
        if self.final_spawn:
            screen.blit(self.image,self.rect)

    def move_down(self,dt):
        self.rect.y += self.speed[1] * dt
        
        if self.rect.y >= HEIGHT:
            self.rect.y = -64

    def move_left_right(self,dt):
        self.rect.x += self.speed[0] * dt

        left_wall:int = self.start_pos[0]
        right_wall:int = self.start_pos[0] + 300 - self.w
        
        if self.rect.x <= left_wall or self.rect.x >= right_wall:
            self.speed[0] *= -1
  
    def reset_bolders(self):
        self.rect.x, self.rect.y = self.start_pos
  
    def update(self,dt):
        self.handle_animations()
        self.move_down(dt)
        self.move_left_right(dt)
        
    def draw(self,screen):
        screen.blit(self.image,self.rect)

final_bolder = The_Bolders(name = "Bolder",
        x = 0,
        y = 350,
        width = 96,
        height = 96,
        direction = "Up",
        frame_count = 3,
        in_room = 2,
        speed = [100,150],
        sheet_size = [387,128])
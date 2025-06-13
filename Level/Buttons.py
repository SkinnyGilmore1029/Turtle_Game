import pygame
from Utility.Image_Handler import data
from The_turtles.The_player import player
from Enemy.The_Villian import boss2

class Button(pygame.sprite.Sprite):
    def __init__(self,x:float, y:float, width:int, height:int,pushed_key:str,name2:str):
        super().__init__()
        self.name = "Red Star"
        self.name2 = name2
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        self.pushed_key = pushed_key
        self.image = data.load_image(self.name)
        self.image = pygame.transform.smoothscale(self.image,(self.w,self.h))
        self.rect = pygame.FRect(self.x,self.y,self.w,self.h)
        self.mask = pygame.mask.from_surface(self.image)
        self.pressed = False
    
    def getting_pressed(self)->bool:
        if not self.pressed and pygame.sprite.collide_mask(self,player) or pygame.sprite.collide_mask(self,boss2):
            self.pressed = True
            self.on_pressed()
            return True
        return False
    
    def on_pressed(self)->None:
        self.name = "Green Star"
        self.image = data.load_image(self.name)
        self.image = pygame.transform.smoothscale(self.image,(self.w,self.h))
        self.mask = pygame.mask.from_surface(self.image)
    
    def update(self):
        ...
        
    def draw(self,screen:pygame.Surface)->None:
        screen.blit(self.image,self.rect)
        
class The_Buttons(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.already_in_level = set()
        self.loaded_rooms = set()
        self.already_on = set()
        
    def get_level_buttons(self,level:int,room:int)->None:
        set_key = ("Buttons",level,room)
        if set_key not in self.loaded_rooms:
            button_data = data.load_level_data(level,"buttons")
            for b in button_data.values():
                if b["in_room"] == room:
                    button = self.create_buttons(b)
                    if b['pushed key'] in self.already_on:
                        button.pressed = True
                        button.on_pressed()
                    self.add(button)
            self.loaded_rooms.add(set_key)
    
    def clear_buttons_level(self):
        self.empty()
        self.already_in_level.clear()
        self.already_on.clear()
        self.loaded_rooms.clear()
        
    def clear_buttons_room(self,level,room):
        self.empty()
        set_key = ("Buttons",level,room)
        if set_key in self.loaded_rooms:
            self.loaded_rooms.remove(set_key)
            
    def create_buttons(self,data:dict)->Button:
        return Button(
            x= data['x'],
            y= data['y'],
            width= data['width'],
            height= data['height'],
            pushed_key= data['pushed key'],
            name2 = data['name']
        )
        
    def check_if_pushed(self)->None:
        for sprite in self:
            if sprite.getting_pressed():
                self.already_on.add((sprite.pushed_key))
    
    def get_already_on_size(self)->int:
        return len(self.already_on)
            
    def update(self)->None:
        self.check_if_pushed()
        
    def draw(self,screen:pygame.Surface)->None:
        for sprite in self:
            sprite.draw(screen)

            
Button_group = The_Buttons()
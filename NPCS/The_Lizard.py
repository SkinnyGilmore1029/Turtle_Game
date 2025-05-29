import pygame
from .Npc_base import Npc_Base
from The_turtles.The_player import player
from Utility.Image_Handler import data

class Lizard(Npc_Base):
    def __init__(self,name:str,x:float,y:float,width:int,height:int,message:str):
        super().__init__(name,x,y,width,height)
        self.have_flies = False
        self.talk = False
        self.message = message
        self.speed:int = 150
        self.should_move = True
    
    def move(self,dt)->None:
        if self.have_flies and self.should_move:
            self.rect.y -= self.speed *dt
            if self.rect.y <= 32:
                self.rect.y = 32
                self.should_move = False
    
    def talk_to_player(self,screen:pygame.Surface)->None:
        self.message_to_player(screen)
    
    def message_to_player(self,screen:pygame.Surface) -> None:
        if self.have_flies == False:
            mes = self.font.render(self.message,True,"Black","White",500)
        else:
            mes = self.font.render("Thank You!",True,"Black","White",500)
        screen.blit(mes,(400,250))
    
    def collision(self):
        if pygame.sprite.collide_mask(self,player):
            if player.rect.top <= self.rect.top:
                player.rect.bottom = self.rect.top
            elif player.rect.bottom >= self.rect.bottom:
                player.rect.top = self.rect.bottom
            elif player.rect.right <= self.rect.right:
                player.rect.right = self.rect.left
            elif player.rect.left >= self.rect.left:
                player.rect.left = self.rect.right
            self.talk = True
        else:
            self.talk = False
    
    def update(self):
        self.collision()
    
    def draw(self,screen:pygame.Surface)->None:
        screen.blit(self.image,self.rect)
        
class The_lizard(pygame.sprite.GroupSingle):
    def __init__(self):
        super().__init__()
        self.flies_collected = 0
    
    def move_lizard_up(self,dt):
        if self.flies_collected == 3:
            self.sprite.have_flies = True
            self.sprite.move(dt)
    
    def get_lizard_data(self,level:int,room:int):
        self.empty()
        lizard_data = data.load_level_data(level,"Npc")["The_Lizard"]
        if lizard_data["in_room"] == room:
            liz =  self.create_lizard(lizard_data)
            self.add(liz)
        
        
    def create_lizard(self,data:dict)->Lizard:
        return Lizard(
            name= data['name'],
            x= data['x'],
            y= data['y'],
            width= data['width'],
            height= data['height'],
            message= data["message" ]
        )
        
    def update(self,dt)->None:
        if self.sprite:
            self.sprite.update()
            self.move_lizard_up(dt)
            
    def draw(self,screen:pygame.Surface)->None:
        if self.sprite:
            self.sprite.draw(screen)
            if self.sprite.talk:
                self.sprite.talk_to_player(screen)
            
Lizards = The_lizard()
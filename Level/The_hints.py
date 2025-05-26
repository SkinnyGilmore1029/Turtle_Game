import pygame
from Utility.Image_Handler import data
from The_turtles.The_player import player
from.Npc_base import Npc_Base

class Hint_Frog(Npc_Base):
    def __init__(self,name:str,x:float,y:float,width:float,height:float,message:str)->None:
        super().__init__(name,x,y,width,height)
        self.message = message
        self.touch = False
        
    def giving_hint(self,screen)->bool:
        self.give_hint_message(screen)
    
    def give_hint_message(self,screen:pygame.Surface)->None:
        mes = self.font.render(self.message,True,"Black","White",450)
        screen.blit(mes,(400,250))

        
class Hint_Group(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        
    def get_level_Npc(self,level:int,room:int)->None:
        self.empty()
        in_level = data.load_level_data(level,"Npc")
        print(in_level)
        for n in in_level.values():
            if n["in_room"] == room:
                npc = self.create_npc(n)
                self.add(npc)
                
    def create_npc(self,data:dict)->object:
        return Hint_Frog(
            name= data["name"],
            x= data['x'],
            y= data["y"],
            width= data["width"],
            height= data["height"],
            message= data['message']
            )
    
    def collison_with_player(self):
        for sprite in self:
            if pygame.sprite.collide_mask(sprite,player):
                sprite.touch = True
                return True
            else:
                sprite.touch = False
                return False

    def update(self)->None:
        self.collison_with_player()

    def draw(self,screen:pygame.Surface)->None:
        for sprite in self:
            sprite.draw(screen)
            if sprite.touch == True:
                sprite.give_hint_message(screen)

The_hints = Hint_Group()
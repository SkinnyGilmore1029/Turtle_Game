
from Utility.Settings import HEIGHT
from .Bad_Guy_Base import Bad_guy


class The_Bolders(Bad_guy):
    def __init__(self,name:str,x:float,y:float,width:int,height:int,direction:str,frame_count:int,in_room:int,speed:list,sheet_size:list)->None:
        super().__init__(name,x,y,width,height,direction,frame_count,in_room,speed,sheet_size)
        
    def move_down(self,dt):
        self.rect.y += self.speed[1] * dt
        
        if self.rect.y >= HEIGHT:
            self.rect.y = -64

    
  
    def update(self,dt):
        self.handle_animations()
        self.move_down(dt)
        
    def draw(self,screen):
        screen.blit(self.image,self.rect)
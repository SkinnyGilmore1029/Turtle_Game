
from Utility.Settings import HEIGHT
from .Bad_Guy_Base import Bad_guy


class The_Bolders(Bad_guy):
    def __init__(self,name:str,x:float,y:float,width:int,height:int,direction:str,frame_count:int,in_room:int,speed:list,sheet_size:list)->None:
        super().__init__(name,x,y,width,height,direction,frame_count,in_room,speed,sheet_size)
        self.start_pos = (x,y)
        
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
import pygame
from .Bad_Guy_Base import Bad_guy


class The_Scorpion(Bad_guy):
    def __init__(self,name:str,x:float,y:float,width:int,height:int,direction:str,frame_count:int,in_room:int,speed:list,sheet_size:list)->None:
        super().__init__(name,x,y,width,height,direction,frame_count,in_room,speed,sheet_size)
        
        
    def pre_load_frames(self):
        """
        Prepares and transforms the player's animation frames for each facing direction.

        This method iterates through the original frames, performing transformations to 
        produce separate frame lists for 'Up', 'Down', 'Left', and 'Right' directions:
            - 'Left': Rotates the image -90 degrees, flips it horizontally, and scales it.
            - 'Right': Rotates the image -90 degrees and scales it.

        The resulting frames are stored in the `transformed_frames` dictionary 
        keyed by direction.
        """
        for frame in self.frames:
            # Up: just scale
            up_img = pygame.transform.smoothscale(frame, (self.w, self.h))
            self.transformed_frames["Up"].append(up_img)
            
            # Down: flip vertically + scale
            down_img = pygame.transform.flip(frame, False, True)
            down_img = pygame.transform.smoothscale(down_img, (self.w, self.h))
            self.transformed_frames["Down"].append(down_img)
            
            # Left: rotate -90 and flip horizontally + scale
            left_img = pygame.transform.rotate(frame, -90)
            left_img = pygame.transform.flip(left_img, True, False)
            left_img = pygame.transform.smoothscale(left_img, (self.w, self.h))
            self.transformed_frames["Left"].append(left_img)
            
            # Right: rotate -90 + scale
            right_img = pygame.transform.rotate(frame, -90)
            right_img = pygame.transform.smoothscale(right_img, (self.w, self.h))
            self.transformed_frames["Right"].append(right_img)
    
    def turn_scorpion_side(self):
        if self.direction == "Left":
            self.image = pygame.transform.rotate(self.image,-90)
            self.image = pygame.transform.flip(self.image,True,False)
        elif self.direction == "Right":
            self.image = pygame.transform.rotate(self.image,-90)
    
    def move(self,dt):
        if self.direction == "Up" or self.direction == "Down":
            self.rect.y -= self.velocity.y *dt
        elif self.direction == "Left" or self.direction == "Right":
            self.rect.x -= self.velocity.x *dt
        
    
    def update(self,dt)->None:
        self.move(dt)
        self.turn_scorpion_side()
        self.handle_animations()
    
    def draw(self,screen:pygame.Surface)->None:
        screen.blit(self.image,self.rect)
import pygame
from Utility.Settings import WIDTH
from Utility.Image_Handler import Image_Animator, get_frames

class Bad_guy(pygame.sprite.Sprite):
    """
    This is a parent Class for all the rest of
    the class that can kill the player.
    """
    def __init__(self,name:str,x:float,y:float,width:int,height:int,direction:str,frame_count:int,in_room:int)->None:
        super().__init__()
        self.name = name
        self.x = x 
        self.y = y
        self.w = width
        self.h = height
        in_room = in_room
        self.rect = pygame.FRect(self.x,self.y,self.w,self.h)
        self.direction = direction
        self.velocity = pygame.Vector2(0,0)
        self.frame_count = frame_count
        self.frames = get_frames(self.name,self.frame_count,self.w,self.h)
        self.animation = Image_Animator(self.name)
        self.transformed_frames = {
            "Left": [],
            "Right": []
        }
        self.pre_load_frames()
        self.current_frame = 0
        self.image = self.transformed_frames[self.direction][self.current_frame]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_timer = pygame.time.get_ticks()
        self.animation_speed = 200  # ms per frame
        
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
            left_img = pygame.transform.flip(frame, True, False)
            left_img = pygame.transform.smoothscale(left_img, (self.w, self.h))
            self.transformed_frames["Left"].append(left_img)
            
            right_img = pygame.transform.smoothscale(frame, (self.w, self.h))
            self.transformed_frames["Right"].append(right_img)
            
    def handle_animations(self)->None:
        """
        Handles player animation frame updates based on elapsed time.

        Advances the animation frame if enough time has passed, and updates 
        the current image and collision mask based on the facing direction.
        """

         # Animate frames over time
        current_time = pygame.time.get_ticks()
        if current_time - self.animation_timer > self.animation_speed:
            self.current_frame = (self.current_frame + 1) % self.frame_count
            self.animation_timer = current_time
        
        # Set current image to the correct frame and direction (no transforms here)
        self.image = self.transformed_frames[self.direction][self.current_frame]
        self.mask = pygame.mask.from_surface(self.image)
 
    def move(self,dt:float)->None:
        #childern class will complete
        pass
        
    def update(self):
        #childern class will complete
        pass
        
    def draw(self,screen:pygame.Surface)->None:
        #childern class will complete
        pass

class The_cars(Bad_guy):
    def __init__(self,name:str,x:float,y:float,width:int,height:int,direction:str,frame_count:int,in_room:int)->None:
        super().__init__(name,x,y,width,height,direction,frame_count,in_room)

    def move(self,dt:float)->None:
        self.velocity.x = 200
        self.rect.x -=self.velocity.x *dt
        if self.rect.x < -128:
            self.rect.x = WIDTH + 30

    def update(self,dt):
        self.move(dt)
        self.handle_animations()
        
    def draw(self,screen:pygame.Surface)->None:
        screen.blit(self.image,self.rect)

test_monster = The_cars("Car", 300,300,128,128,"Right",3,1)
import pygame
from Utility.Image_Handler import Image_Animator, data


class Bad_guy(pygame.sprite.Sprite):
    """
    This is a parent Class for all the rest of
    the class that can kill the player.
    """
    def __init__(self,name:str,x:float,y:float,width:int,height:int,direction:str,frame_count:int,in_room:int,speed:list,sheet_size:list)->None:
        super().__init__()
        self.name = name
        self.x = x 
        self.y = y
        self.w = width
        self.h = height
        self.in_room = in_room
        self.sheet_size = sheet_size
        self.rect = pygame.FRect(self.x,self.y,self.w,self.h)
        self.direction = direction
        self.speed:list[int,int] = speed
        self.velocity = pygame.Vector2(speed[0],speed[1])
        self.frame_count = frame_count
        self.frames = data.get_frames(self.name,self.frame_count,self.w,self.h,self.sheet_size)
        self.animation = Image_Animator(self.name)
        self.transformed_frames = {
            "Left": [],
            "Right": [],
            "Up" : [],
            "Down" : []
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
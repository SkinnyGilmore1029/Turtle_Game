import pygame
from Managers.Image_Manager import Image_Animator
from Managers.Data_Manager import data

def trim_surface(surf: pygame.Surface) -> pygame.Surface:
        """Returns a cropped version of surf removing fully transparent edges."""
        mask = pygame.mask.from_surface(surf)
        rects = mask.get_bounding_rects()
        if rects:
            rect = rects[0]  # get bounding rect of visible pixels
            return surf.subsurface(rect).copy()  # copy to avoid referencing original
        else:
            return surf.copy()
        
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
        self.animation = Image_Animator(self.name)
        self.frames = self.animation.get_frames(self.name,self.frame_count,self.w,self.h,self.sheet_size)
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
        for frame in self.frames:
            trimmed_frame = trim_surface(frame)  # trim transparent edges

            # Up: just scale
            up_img = pygame.transform.smoothscale(trimmed_frame, (self.w, self.h))
            self.transformed_frames["Up"].append(up_img)

            # Down: flip vertically + scale
            down_img = pygame.transform.flip(trimmed_frame, False, True)
            down_img = pygame.transform.smoothscale(down_img, (self.w, self.h))
            self.transformed_frames["Down"].append(down_img)

            # Left: flip horizontally + scale
            left_img = pygame.transform.flip(trimmed_frame, True, False)
            left_img = pygame.transform.smoothscale(left_img, (self.w, self.h))
            self.transformed_frames["Left"].append(left_img)

            # Right: just scale
            right_img = pygame.transform.smoothscale(trimmed_frame, (self.w, self.h))
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
        #children class will complete
        pass

    def update(self):
        #children class will complete
        pass

    def draw(self,screen:pygame.Surface)->None:
        #children class will complete
        pass
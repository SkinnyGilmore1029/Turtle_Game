import pygame
from Utility.Image_Handler import data,Image_Animator

class Npc_Base(pygame.sprite.Sprite):
    def __init__(self,name:str,x:float,y:float,width:float,height:float)->None:
        super().__init__()
        self.name = name
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        self.image = data.load_image(name)
        self.image = pygame.transform.smoothscale(self.image,(self.w,self.h))
        self.rect = pygame.FRect(self.x,self.y,self.w,self.h)
        self.mask = pygame.mask.from_surface(self.image)
        self.font = pygame.font.SysFont("Arial",24,True)
        
    def upadat(self):
        #update will be filled in with childern class methods
        pass
    
    def draw(self,screen:pygame.Surface)->None:
        screen.blit(self.image,self.rect)
        
class Animated_Npc_base(pygame.sprite.Sprite):
    def __init__(self, name:str, x:float, y:float,width:int, height:int,direction:str,frame_count:int,sheet_size:list)->None:
        super().__init__()
        self.name = name
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        self.sheet_size = sheet_size
        self.rect = pygame.FRect(self.x,self.y,self.w,self.h)
        self.direction = direction
        self.velocity = pygame.Vector2(0,0)
        self.frame_count = frame_count
        self.frames = data.get_frames(self.name,self.frame_count,self.w,self.h,self.sheet_size)
        self.animation = Image_Animator(self.name)
        self.transformed_frames = {
            "Up": [],
            "Down": [],
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
            - 'Up': Scales the original image.
            - 'Down': Flips the image vertically and scales it.
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
           
    def update(self, dt):
        #will be updated by children classes
        pass
    
    def draw(self,screen:pygame.Surface)->None:
        #will be updated by children classes
        pass
        

            
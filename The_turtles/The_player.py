import pygame
from Utility.Settings import WIDTH,HEIGHT
from Utility.Image_Handler import Image_Animator, data

class Player(pygame.sprite.Sprite):
    """
        Represents the player-controlled character sprite in a Pygame-based game.

        This class manages the player's position, movement, animation, and rendering.
        It responds to keyboard inputs for directional movement and updates the player's 
        animation frames based on the facing direction.

        Attributes:
            lives (int): Number of lives the player has. Shared by all instances.
            name (str): The name of the sprite sheet (without extension) to load.
            x (float): Initial X position of the player.
            y (float): Initial Y position of the player.
            w (int): Width of each animation frame.
            h (int): Height of each animation frame.
            rect (pygame.FRect): The player's rectangular position and size for positioning and collision.
            direction (str): Current facing direction ('Up', 'Down', 'Left', 'Right').
            velocity (pygame.Vector2): The player's velocity in both axes.
            frame_count (int): Number of animation frames per direction.
            frames (list): List of raw frames loaded from the sprite sheet.
            animation (Image_Animator): Image animator helper instance (not actively used yet here).
            transformed_frames (dict): Pre-transformed images for each direction.
            current_frame (int): Index of the current animation frame.
            image (pygame.Surface): Current image of the player.
            mask (pygame.Mask): Collision mask for the current image.
            animation_timer (int): Time of the last frame change.
            animation_speed (int): Milliseconds between animation frames.
        """
    lives:int = 5
    def __init__(self, name:str, x:float, y:float,width:int, height:int,direction:str,frame_count:int)->None:
        """
        Initializes a new Player instance.

        Parameters:
            name (str): The name of the sprite sheet image file to load (without extension).
            x (float): Starting X position of the player.
            y (float): Starting Y position of the player.
            width (int): Width of each animation frame.
            height (int): Height of each animation frame.
            direction (str): Initial facing direction ('Up', 'Down', 'Left', 'Right').
            frame_count (int): Number of animation frames per direction.
        """

        super().__init__()
        self.name = name
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        self.rect = pygame.FRect(self.x,self.y,self.w,self.h)
        self.direction = direction
        self.velocity = pygame.Vector2(0,0)
        self.frame_count = frame_count
        self.frames = data.get_frames(self.name,self.frame_count,self.w,self.h)
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
        
        
    def move(self,dt:float)->None:
        """
        Updates the player's velocity and position based on keyboard input.

        This method checks the current keyboard state and sets the player's 
        velocity and facing direction accordingly. The player's position is 
        then updated using the velocity scaled by the delta time (dt) for 
        framerate-independent movement.

        Parameters:
            dt (float): Time elapsed since the last frame (delta time).
        """

        keys = pygame.key.get_pressed()
        self.velocity.x = 0
        self.velocity.y = 0

        if keys[pygame.K_LEFT]:
            self.velocity.x = -200
            self.direction = "Left"
        if keys[pygame.K_RIGHT]:
            self.velocity.x = 200
            self.direction = "Right"
        if keys[pygame.K_UP]:
            self.velocity.y = -200
            self.direction = "Up"
        if keys[pygame.K_DOWN]:
            self.velocity.y = 200
            self.direction = "Down"

        self.rect.x += self.velocity.x * dt
        self.rect.y += self.velocity.y * dt
    
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
    
    
    def died(self):
        self.lives -= 1
        self.rect.x = self.x
        self.rect.y = self.y
    
    def update(self, dt):
        """
        Updates the player's state.

        Calls movement and animation handling methods.

        Parameters:
            dt (float): Time elapsed since the last frame (delta time).
        """

        # Move player
        self.move(dt)
        self.handle_animations()
    
    def draw(self,screen:pygame.Surface)->None:
        """
        Draws the player's current image at its position on the given surface.

        Parameters:
            screen (pygame.Surface): The surface to draw the player onto.
        """
        screen.blit(self.image,self.rect)
        
player = Player("Turtle",WIDTH*.5,HEIGHT-64,64,64,"Up",3)
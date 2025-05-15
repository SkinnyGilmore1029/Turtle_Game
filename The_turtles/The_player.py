import pygame
from Utility.Image_Handler import Image_Animator, get_frames

class Player(pygame.sprite.Sprite):
    """
    A player-controlled character sprite for a Pygame-based game.

    This class handles the player's position, movement, direction, and rendering. 
    It responds to keyboard input for directional movement and updates the 
    character's image based on the current facing direction.

    Attributes:
        name (str): The name of the sprite image file (without extension) to load.
        x (float): The initial X position of the player on the screen.
        y (float): The initial Y position of the player on the screen.
        w (int): The width of the player's sprite.
        h (int): The height of the player's sprite.
        rect (pygame.FRect): The player's rectangular position and size for positioning and collision.
        direction (str): The current facing direction of the player ('Up', 'Down', 'Left', 'Right').
        velocity (pygame.Vector2): The current velocity of the player for movement.
        image (pygame.Surface): The current image of the player (set in `direction_facing()`).
        mask (pygame.Mask): The collision mask generated from the current image.
    """
    lives:int = 5
    def __init__(self, name:str, x:float, y:float,width:int, height:int,direction:str,frame_count:int)->None:
        """
        Initializes a new Player instance.

        Parameters:
            name (str): The name of the image file to load for the player.
            x (float): The starting X position of the player.
            y (float): The starting Y position of the player.
            width (int): The width of the player's sprite.
            height (int): The height of the player's sprite.
            direction (str): The initial facing direction of the player ('Up', 'Down', 'Left', 'Right').
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
        self.frames = get_frames(self.name,self.frame_count,self.w,self.h)
        self.animation = Image_Animator(self.name)
        self.animation.frames = self.frames
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
        Updates the character's velocity and position based on user input.

        This method checks the current keyboard state for arrow key inputs and 
        sets the character's velocity and facing direction accordingly.
        It then updates the character's position (`self.rect`) based on the 
        velocity and delta time (`dt`).
        
        Parameters:
            dt (float): The time elapsed since the last frame (delta time),
                        used to scale movement speed for frame rate independence.
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
    
    def update(self, dt):
        # Move player
        self.move(dt)
        
        # Animate frames over time
        current_time = pygame.time.get_ticks()
        if current_time - self.animation_timer > self.animation_speed:
            self.current_frame = (self.current_frame + 1) % self.frame_count
            self.animation_timer = current_time
        
        # Set current image to the correct frame and direction (no transforms here)
        self.image = self.transformed_frames[self.direction][self.current_frame]
        self.mask = pygame.mask.from_surface(self.image)
    
    def draw(self,screen:pygame.Surface)->None:
        screen.blit(self.image,self.rect)
        
player = Player("Turtle",200,200,64,64,"Up",3)
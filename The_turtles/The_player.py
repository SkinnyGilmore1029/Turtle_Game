import pygame
from Utility.Settings import WIDTH,HEIGHT
from Utility.Image_Handler import load_image

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
    def __init__(self, name:str, x:float, y:float,width:int, height:int,direction:str)->None:
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
        self.image = None
        self.mask = None

    def direction_facing(self)->None:
        """
        Updates the character's image based on their current facing direction.

        This method reloads the base image for the character using `load_image(self.name)`
        and applies transformations (scaling, flipping, and rotating) depending on the 
        value of `self.direction` ('Up', 'Down', 'Left', 'Right'). 
        Also creates a new mask from the transformed image for collision detection.
        """
        self.image = load_image(self.name)
        match self.direction:
            case "Up":
                self.image = pygame.transform.smoothscale(self.image,(self.w,self.h))
            case "Down":
                self.image = pygame.transform.flip(load_image(self.name),False,True)
                self.image = pygame.transform.smoothscale(self.image,(self.w,self.h))
            case "Left":
                self.image = pygame.transform.rotate(self.image, -90.0)
                self.image = pygame.transform.flip(self.image, True, False)
                self.image = pygame.transform.smoothscale(self.image, (self.w, self.h))
            case "Right":
                self.image = pygame.transform.rotate(self.image, -90.0)
                self.image = pygame.transform.smoothscale(self.image, (self.w, self.h))
        self.mask = pygame.mask.from_surface(self.image)
        
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
            self.image = None
            self.velocity.x = -200
            self.direction = "Left"
        if keys[pygame.K_RIGHT]:
            self.image = None
            self.velocity.x = 200
            self.direction = "Right"
        if keys[pygame.K_UP]:
            self.image = None
            self.velocity.y = -200
            self.direction = "Up"
        if keys[pygame.K_DOWN]:
            self.image = None
            self.velocity.y = 200
            self.direction = "Down"

        self.rect.x += self.velocity.x * dt
        self.rect.y += self.velocity.y * dt
        
    def draw(self,screen:pygame.Surface,dt:float)->None:
        """
        Handles updating and rendering the character on the screen.

        This method first updates the character's position and direction by calling
        `move()` and `direction_facing()`, then draws the character's image at the 
        current position on the provided screen surface.

        Parameters:
            screen (pygame.Surface): The surface to draw the character on.
            dt (float): The time elapsed since the last frame (delta time),
                        passed to the `move()` method for frame rate independent movement.
        """
        self.move(dt)
        self.direction_facing()
        screen.blit(self.image,self.rect)
        
player = Player("Turtle",200,200,64,64,"Up")
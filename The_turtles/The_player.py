import pygame
from Utility.Settings import HEIGHT,CUTSCENE_POS,LEVEL1_POS
from .Turtle_base import Turtle_Base

class Player(Turtle_Base):
    def __init__(self, name:str, x:float, y:float,width:int, height:int,direction:str,frame_count:int)->None:
        super().__init__(name,x,y,width,height,direction,frame_count)
        self.lives = 5
        self.key_count = 0
        self.speed = 300
        self.chase = False
        self.scaled = False
        
        
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
            self.velocity.x = -self.speed
            self.direction = "Left"
        if keys[pygame.K_RIGHT]:
            self.velocity.x = self.speed
            self.direction = "Right"
        if keys[pygame.K_UP]:
            self.velocity.y = -self.speed
            self.direction = "Up"
        if keys[pygame.K_DOWN]:
            self.velocity.y = self.speed
            self.direction = "Down"

        self.rect.x += self.velocity.x * dt
        self.rect.y += self.velocity.y *dt
    
    def move_cutscene(self,dt,game):
        self.velocity.y = 0
        if self.chase is True:
            self.velocity.y = self.speed
            self.direction = "Down"
        self.rect.y += self.velocity.y *dt
        
        if self.rect.y > HEIGHT:
            game.game_state = "Playing"
            self.w = 64
            self.h = 64
            self.rect.x = LEVEL1_POS[0]
            self.rect.y = LEVEL1_POS[1]
            self.direction = "Up"
        
    def update_cutscene(self,dt,game):
        self.move_cutscene(dt,game)
        self.handle_animations()

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
        
player = Player("Turtle",CUTSCENE_POS[0],CUTSCENE_POS[1],64,64,"Up",3)
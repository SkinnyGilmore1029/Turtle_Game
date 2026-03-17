import pygame
from Utility.Settings import HEIGHT,CUTSCENE_POS,LEVEL1_POS
from .Turtle_base import Turtle_Base

class Player(Turtle_Base):
    def __init__(self, name:str, x:float, y:float,width:int, height:int,direction:str,frame_count:int,sheet_size:list)->None:
        super().__init__(name,x,y,width,height,direction,frame_count,sheet_size)
        self.lives = 15
        self.key_count = 0
        self.speed = 300
        self.chase = False
        self.scaled = False
        self.button_pushed: dict[str, bool] = {
            "up" : False,
            "down" : False,
            "left" : False,
            "right" : False,
            "control up" : False,
            "control down" : False,
            "control left" : False,
            "control right" : False
        }

    def get_player_pos(self) -> tuple[int,int]:
        return (self.x, self.y)

    def move_up(self, dt:float) -> None:
        if self.button_pushed["up"] or self.button_pushed['control up']:
            self.direction = "Up"
            self.velocity.y = -self.speed
            self.rect.y += self.velocity.y *dt
            #self.button_pushed['up'] = False


    def move_down(self,dt:float) -> None:
        if self.button_pushed["down"] or self.button_pushed['control down']:
            self.velocity.y = self.speed
            self.direction = "Down"
            self.rect.y += self.velocity.y *dt
            #self.button_pushed['down'] = False


    def move_left(self, dt:float) -> None:
        if self.button_pushed["left"]or self.button_pushed['control left']:
            self.velocity.x = -self.speed
            self.direction = "Left"
            self.rect.x += self.velocity.x * dt
            #self.button_pushed['left'] = False

    def move_right(self, dt:float) -> None:
        if self.button_pushed["right"] or self.button_pushed['control right']:
            self.velocity.x = self.speed
            self.direction = "Right"
            self.rect.x += self.velocity.x * dt
            #self.button_pushed['right'] = False


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

    def died(self,level_pos:tuple[int,int])->None:
        self.lives -= 1
        self.rect.x = level_pos[0]
        self.rect.y = level_pos[1]

    def update(self, dt):
        """
        Updates the player's state.

        Calls movement and animation handling methods.

        Parameters:
            dt (float): Time elapsed since the last frame (delta time).
        """

        self.move_down(dt)
        self.move_up(dt)
        self.move_left(dt)
        self.move_right(dt)
        self.handle_animations()

    def draw(self,screen:pygame.Surface)->None:
        """
        Draws the player's current image at its position on the given surface.

        Parameters:
            screen (pygame.Surface): The surface to draw the player onto.
        """
        screen.blit(self.image,self.rect)

player = Player("Turtle",CUTSCENE_POS[0],CUTSCENE_POS[1],64,64,"Up",3,[192,64])
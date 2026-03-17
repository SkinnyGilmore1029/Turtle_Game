import pygame
from .Image_Manager import my_image

class Cursor(pygame.sprite.Sprite):
    def __init__(self,option_name:str,x:int,y:int):
        super().__init__()
        self.option_name = option_name
        self.x = x
        self.y = y
        self.w = 32
        self.h = 32
        self.image = my_image.load_image("Cursor")
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.selected_index: int = 0

    def move_up(self, option_list:list[str|int], y_start:int, y_spacing:int, x_spacing:int) -> None:
        """Moves the cursor to the next position in the list.

        Args:
            option_list (list[str | int]): The list of option names for the screen.
            y_start (int): Where the cursor needs to start for the rect.y
            y_spacing (int): How far apart are the list options on the screen.
            x_spacing (int): For screens that need to move the cursor left or right.
        """
        self.selected_index = (self.selected_index - 1) % len(option_list)
        self.update(option_list, y_start, y_spacing, x_spacing)

    def move_down(self, option_list:list[str|int], y_start:int, y_spacing:int, x_spacing:int) -> None:
        """Moves the cursor to the next position in the list.

        Args:
            option_list (list[str | int]): The list of option names for the screen.
            y_start (int): Where the cursor needs to start for the rect.y
            y_spacing (int): How far apart are the list options on the screen.
            x_spacing (int): For screens that need to move the cursor left or right.
        """
        self.selected_index = (self.selected_index + 1) % len(option_list)
        self.update(option_list, y_start, y_spacing, x_spacing)

    def update(self, option_list:list[str|int], y_start:int, y_spacing:int, x_spacing:int) -> None:
        """Updates the cursor position on that will be displayed on the screen.

        Args:
            option_list (list[str | int]): The list of option names for the screen.
            y_start (int): Where the cursor needs to start for the rect.y
            y_spacing (int): How far apart are the list options on the screen.
            x_spacing (int): For screens that need to move the cursor left or right.
        """
        self.option_name = option_list[self.selected_index]
        self.rect.x = x_spacing - self.w
        self.rect.y = y_start+ (self.selected_index * y_spacing)

    def draw_cursor(self,screen:pygame.Surface)->None:
        """Draws the cursor on to the screen.

        Args:
            screen (pygame.Surface): The screen you want the cursor on.
        """
        screen.blit(self.image,self.rect)
import pygame
from .Screen_base import Screens
from Managers.Image_Manager import my_image
from Managers.Cursor_Manager import Cursor

class Title(Screens):
    def __init__(self,name:str)->None:
        super().__init__(name)
        self.background = my_image.load_image(name)
        self.y_start: int = 640
        self.y_space: int = 80
        self.x_start: int = 500
        self.cursor: Cursor = Cursor("New Game", self.x_start - 32, 640)
        self.button_pushed: dict[str, bool] = {
            "n" : False,
            "l" : False,
            "Joystick up": False,
            "Joystick down" : False,
            "Controller A" : False
        }
        self.option_names: list[str] = ["New Game", "Level Select"]
        self.color: str = "#F5E800"

    def begin_game(self,game:object)->None:
        """Starts a new game using the Keyboard.

        Args:
            game (object): The main game class.
        """
        if self.button_pushed["n"]:
            game.playing = True
            game.game_state = "Starting Cutscene"
            self.button_pushed['n'] = False

    def choose_level(self,game:object)->None:
        """Opens the level select screen using
        the keyboard.

        Args:
            game (object): The main game class.
        """
        if self.button_pushed["l"]:
            game.game_state = "Choosing Level"
            self.button_pushed["l"] = False

    def move_cursor_up(self) ->None:
        """Helps control the up press on
        the joystick on the controller.
        """
        if self.button_pushed["Joystick up"]:
            self.cursor.move_up(self.option_names,
                                self.y_start,
                                self.y_space,
                                self.x_start)
            self.button_pushed["Joystick up"] = False

    def move_cursor_down(self) ->None:
        """Helps control the down press on
        the joystick on the controller.
        """
        if self.button_pushed["Joystick down"]:
            self.cursor.move_down(self.option_names,
                                self.y_start,
                                self.y_space,
                                self.x_start)
            self.button_pushed["Joystick down"] = False

    def select_option_controller(self, game:object):
        """Helps handle button presses that
        select the option the cursor is on.

        Args:
            game (object): The main game class.
        """
        if self.button_pushed["Controller A"] and self.cursor.option_name == "New Game":
            game.playing = True
            game.game_state = "Starting Cutscene"
            self.button_pushed["Controller A"] = False
        elif self.button_pushed["Controller A"] and self.cursor.option_name == "Level Select":
            game.game_state = "Choosing Level"
            self.button_pushed["Controller A"] = False

    def Title_screen_text(self, screen:pygame.Surface) -> None:
        """Displays the Title of the Game on the Screen

        Args:
            screen (pygame.Surface): The surface you want to draw on.
        """
        Title = self.fonts["Title"].render("Squartle Quest!",True,self.color)
        screen.blit(Title,(440,40))

    def Title_screen_options(self, screen:pygame.Surface) -> None:
        """Displays the controls for the Title Screen.

        Args:
            screen (pygame.Surface): The surface you want to draw on.
        """
        for i, texts in enumerate(self.option_names):
            text = self.fonts["Start Button"].render(texts,True, self.color)
            y_pos = self.y_start + i * self.y_space
            screen.blit(text,(self.x_start,y_pos))

    def update_cursor(self):
        self.move_cursor_down()
        self.move_cursor_up()

    def Title_screen_controls(self,game)->None:
        self.select_option_controller(game)
        self.choose_level(game)
        self.begin_game(game)

    def draw_Title_screen(self,screen:pygame.Surface)->None:
        screen.blit(self.background,(0,0))
        self.cursor.draw_cursor(screen)
        self.Title_screen_text(screen)
        self.Title_screen_options(screen)

Title_screen = Title('Title Screen')
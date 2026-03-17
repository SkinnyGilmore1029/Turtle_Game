import pygame
from .Screen_base import Screens
from The_turtles.The_player import player
from Utility.Settings import (
    LEVEL1_POS,
    LEVEL2_POS,
    LEVEL3_POS,
    LEVEL4_POS,
    LEVEL5_POS,
    LEVEL6_POS,
    LEVEL7_POS,
    LEVEL8_POS
)
from Managers.Cursor_Manager import Cursor

class Choose_Level(Screens):
    def __init__(self,name:str)->None:
        super().__init__(name)
        self.cursor: Cursor = Cursor("Level 1", 168, 200)
        self.button_pushed: dict[int|str, bool] = {
            1: False,
            2: False,
            3: False,
            4: False,
            5: False,
            6: False,
            7: False,
            8: False,
            "Esc" : False,
            "D-Pad up" : False,
            "D-pad down" : False,
            "Controller B" : False,
            "Controller A" : False
        }
        self.starting_pos:int = 200
        self.y_spacing:int = 40
        self.color: str = "#F5E800"

    def choose_level_up(self) -> None:
        """Helps control the up press on
        the joystick on the controller.
        """
        if self.button_pushed["D-Pad up"]:
            self.cursor.move_up([f"Level {i + 1}" for i, _ in enumerate(range(8))],
                                self.starting_pos,
                                self.y_spacing,
                                self.starting_pos)
            self.button_pushed["D-Pad up"] = False

    def choose_level_down(self) -> None:
        """Helps control the down press on
        the joystick on controller.
        """
        if self.button_pushed["D-pad down"]:
            self.cursor.move_down([f"Level {i + 1}" for i, _ in enumerate(range(8))],
                                self.starting_pos,
                                self.y_spacing,
                                self.starting_pos)
            self.button_pushed["D-pad down"] = False

    def get_level_from_cursor(self) -> int:
        """Takes the selected level from the cursor
        and converts in to an integer for choosing_level.

        Returns:
            int: The level number.
        """
        match self.cursor.option_name:
            case "Level 1":
                return 1
            case "Level 2":
                return 2
            case "Level 3":
                return 3
            case "Level 4":
                return 4
            case "Level 5":
                return 5
            case "Level 6":
                return 6
            case "Level 7":
                return 7
            case "Level 8":
                return 8

    def choosing_level(self, game: object) -> None:
        """Handles the level selection for both
        keyboard and controller.

        Args:
            game (object): The main game class.
        """
        if game.room != 1:
            game.room = 1

        # Map level numbers to their positions
        level_positions = {
            1: LEVEL1_POS,
            2: LEVEL2_POS,
            3: LEVEL3_POS,
            4: LEVEL4_POS,
            5: LEVEL5_POS,
            6: LEVEL6_POS,
            7: LEVEL7_POS,
            8: LEVEL8_POS
        }

        # Loop through button_pushed
        for key, pressed in self.button_pushed.items():
            if pressed:
                if key == "Esc" or key == "Controller B":
                    game.game_state = "Title"
                elif key == "D-pad down" or key == "D-pad up":
                    continue
                else:
                    level_key = self.get_level_from_cursor()
                    game.level = level_key
                    game.playing = True
                    game.game_state = "Playing"
                    player.rect.x, player.rect.y = level_positions[level_key]
                # Reset the button
                self.button_pushed[key] = False
                break

    def Title_Text(self, screen:pygame.Surface) -> None:
        """Displays the Title of the game on the screen.

        Args:
            screen (pygame.Surface): The screen you want to display on.
        """
        Title = self.fonts["Title"].render("Choose Your Level!",True,self.color)
        screen.blit(Title,(400,0))

    def explain_text(self, screen: pygame.Surface)-> None:
        """Displays what the controls are on the level selection
        screen.

        Args:
            screen (pygame.Surface): The screen you want to display on.mo
        """
        pygame.draw.rect(screen,"Black", (680, 180, 510, 430), 20, 10, 10, 10, 10, 10)
        explain_text = self.fonts["Start Button"].render("Press the number of the level on the Keyboard to choose!",True,self.color,None,500)
        control_text = self.fonts["Start Button"].render("Move the cursor to the level and press A",True,self.color,None,400)
        back = self.fonts["Start Button"].render("Press the Escape button or the B button to go back to Title Screen",True,self.color,None,500)
        screen.blits([
            (explain_text,(700,200)),
            (control_text,(700,350)),
            (back, (700, 500))
            ])

    def update_cursor(self) -> None:
        """Changes the position and
        option name of the cursor.
        """
        self.choose_level_up()
        self.choose_level_down()

    def draw_option_text(self, screen: pygame.Surface) -> None:
        """Displays the Level options on the screen.

        Args:
            screen (pygame.Surface): The screen you want to display on.
        """
        for i, _ in enumerate(range(8)):
            level = self.fonts["Start Button"].render(f"Level {i +1 }",True,self.color)
            y_pos = self.starting_pos + i * self.y_spacing
            screen.blit(level,(self.starting_pos,y_pos))

    def draw_choose_level_screen(self,screen: pygame.Surface)->None:
        """Displays Everything together for the main loop.

        Args:
            screen (pygame.Surface): The screen you want to display on.
        """
        screen.fill("Blue")
        self.cursor.draw_cursor(screen)
        self.explain_text(screen)
        self.Title_Text(screen)
        self.draw_option_text(screen)


Choosing_screen = Choose_Level('Title Screen')
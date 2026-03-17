import pygame
from UI.Choosing_Screen import Choosing_screen
from UI.Title_screen import Title_screen
from The_turtles.The_player import player

class KeyBoardManager:

    def start_screen_keyboard(self, event: pygame.Event) -> None:
        """Handles the keyboard input events for the Title Screen.

        Args:
            event (pygame.Event): The keyboard input.
        """
        if event.type != pygame.KEYDOWN:
            return
        match event.key:
            case pygame.K_n:
                Title_screen.button_pushed["n"] = True
            case pygame.K_l:
                Title_screen.button_pushed["l"] = True

    def move_turtle_keyboard(self, event: pygame.Event, game:object) -> None:
        """Handles the keyboard input events for moving the player around.

        Args:
            event (pygame.Event): The keyboard input.
            game (object): The main game class.
        """
        if event.type != pygame.KEYDOWN and event.type != pygame.KEYUP:
            return
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_UP:
                    player.button_pushed["up"] = True
                case pygame.K_DOWN:
                    player.button_pushed["down"] = True
                case pygame.K_LEFT:
                    player.button_pushed["left"] = True
                case pygame.K_RIGHT:
                    player.button_pushed["right"] = True
        elif event.type == pygame.KEYUP:
            match event.key:
                case pygame.K_UP:
                    player.button_pushed["up"] = False
                case pygame.K_DOWN:
                    player.button_pushed["down"] = False
                case pygame.K_LEFT:
                    player.button_pushed["left"] = False
                case pygame.K_RIGHT:
                    player.button_pushed["right"] = False

    def handle_choosing_keyboard(self, event: pygame.Event) -> None:
        """Handles the keyboard input events for the level selection screen.

        Args:
            event (pygame.Event): The keyboard input.
        """
        if event.type != pygame.KEYDOWN:
            return
        match event.key:
            case pygame.K_1:
                Choosing_screen.button_pushed[1] = True
                Choosing_screen.cursor.option_name = "Level 1"
            case pygame.K_2:
                Choosing_screen.button_pushed[2] = True
                Choosing_screen.cursor.option_name = "Level 2"
            case pygame.K_3:
                Choosing_screen.button_pushed[3] = True
                Choosing_screen.cursor.option_name = "Level 3"
            case pygame.K_4:
                Choosing_screen.button_pushed[4] = True
                Choosing_screen.cursor.option_name = "Level 4"
            case pygame.K_5:
                Choosing_screen.button_pushed[5] = True
                Choosing_screen.cursor.option_name = "Level 5"
            case pygame.K_6:
                Choosing_screen.button_pushed[6] = True
                Choosing_screen.cursor.option_name = "Level 6"
            case pygame.K_7:
                Choosing_screen.button_pushed[7] = True
                Choosing_screen.cursor.option_name = "Level 7"
            case pygame.K_8:
                Choosing_screen.button_pushed[8] = True
                Choosing_screen.cursor.option_name = "Level 8"
            case pygame.K_ESCAPE:
                Choosing_screen.button_pushed["Esc"] = True

the_keyboard = KeyBoardManager()
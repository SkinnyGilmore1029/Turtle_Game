import pygame
from UI.Choosing_Screen import Choosing_screen

class KeyBoardManager:

    def start_screen_keyboard(self, event: pygame.Event, game:object) -> None:
        if event.type != pygame.KEYDOWN:
            return

    def move_turtle_keyboard(self, event: pygame.Event, game:object) -> None:
        if event.type != pygame.KEYDOWN:
            return

    def handle_choosing_keyboard(self, event: pygame.Event, game:object) -> None:
        if event.type != pygame.KEYDOWN:
            return
        match event.key:
            case pygame.K_1:
                Choosing_screen.button_pushed[1] = True
            case pygame.K_2:
                Choosing_screen.button_pushed[2] = True
            case pygame.K_3:
                Choosing_screen.button_pushed[3] = True
            case pygame.K_4:
                Choosing_screen.button_pushed[4] = True
            case pygame.K_5:
                Choosing_screen.button_pushed[5] = True
            case pygame.K_6:
                Choosing_screen.button_pushed[6] = True
            case pygame.K_7:
                Choosing_screen.button_pushed[7] = True
            case pygame.K_8:
                Choosing_screen.button_pushed[8] = True
            case pygame.K_ESCAPE:
                Choosing_screen.button_pushed["Esc"] = True

the_keyboard = KeyBoardManager()
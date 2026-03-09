import pygame
from The_turtles.The_player import player


class Controller_Events:
    controller_buttons: dict[str, int] = {
        "A": 0,
        "B": 1,
        "X": 2,
        "Y": 3,
        "Left Trigger" : 4,
        "Right Trigger" : 5,
        "Select" : 6,
        "Start": 7
    }

    def player_controller(self, event: pygame.Event) -> None:
        DEADZONE = 0.3

        if event.type == pygame.JOYAXISMOTION:

            # Left stick horizontal
            if event.axis == 0:

                player.button_pushed["left"] = event.value < -DEADZONE
                player.button_pushed["right"] = event.value > DEADZONE

            # Left stick vertical
            elif event.axis == 1:

                player.button_pushed["up"] = event.value < -DEADZONE
                player.button_pushed["down"] = event.value > DEADZONE

the_controller: Controller_Events = Controller_Events()

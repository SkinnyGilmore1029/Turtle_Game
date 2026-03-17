import pygame
from The_turtles.The_player import player
from UI.Choosing_Screen import Choosing_screen


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
    DEADZONE = 0.3

    def player_controller(self, event: pygame.Event) -> None:
        if event.type == pygame.JOYAXISMOTION:

            # Left stick horizontal
            if event.axis == 0:

                player.button_pushed["left"] = event.value < -self.DEADZONE
                player.button_pushed["right"] = event.value > self.DEADZONE

            # Left stick vertical
            elif event.axis == 1:

                player.button_pushed["up"] = event.value < -self.DEADZONE
                player.button_pushed["down"] = event.value > self.DEADZONE

    def choose_screen_controller(self, event: pygame.Event) -> None:
        if event.type == pygame.JOYAXISMOTION and event.axis == 1:
            Choosing_screen.button_pushed["D-Pad up" ] = event.value < -self.DEADZONE
            Choosing_screen.button_pushed["D-pad down"] = event.value > self.DEADZONE
        elif event.type == pygame.JOYBUTTONDOWN and event.button == self.controller_buttons["B"]:
            Choosing_screen.button_pushed["Controller B"] = True
        elif event.type == pygame.JOYBUTTONDOWN and event.button == self.controller_buttons["A"]:
            Choosing_screen.button_pushed["Controller A"] = True

the_controller: Controller_Events = Controller_Events()

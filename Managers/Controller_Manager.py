import pygame
from The_turtles.The_player import player
from UI.Choosing_Screen import Choosing_screen
from UI.Title_screen import Title_screen


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
    def __init__(self):
        self.stick_locked: bool = False

    def player_controller(self, event: pygame.Event) -> None:
        DEADZONE = 0.3
        if event.type == pygame.JOYAXISMOTION:

            # Left stick horizontal
            if event.axis == 0:

                player.button_pushed["control left"] = event.value < -DEADZONE
                player.button_pushed["control right"] = event.value > DEADZONE

            # Left stick vertical
            elif event.axis == 1:

                player.button_pushed["control up"] = event.value < -DEADZONE
                player.button_pushed["control down"] = event.value > DEADZONE

    def choose_screen_controller(self, event: pygame.Event) -> None:
        DEADZONE = 0.3
        if event.type == pygame.JOYAXISMOTION and event.axis == 1:
            if event.value < -DEADZONE and not self.stick_locked:
                Choosing_screen.button_pushed["D-Pad up"] = True
                self.stick_locked = True
            elif event.value > DEADZONE and not self.stick_locked:
                Choosing_screen.button_pushed["D-pad down"] = True
                self.stick_locked = True
            elif -DEADZONE < event.value < DEADZONE:
                self.stick_locked = False
        elif event.type == pygame.JOYBUTTONDOWN and event.button == self.controller_buttons["B"]:
            Choosing_screen.button_pushed["Controller B"] = True
        elif event.type == pygame.JOYBUTTONDOWN and event.button == self.controller_buttons["A"]:
            Choosing_screen.button_pushed["Controller A"] = True

    def title_screen_controller(self, event: pygame.Event) -> None:
        DEADZONE = 0.3
        if event.type == pygame.JOYAXISMOTION and event.axis == 1:
            if event.value < -DEADZONE and not self.stick_locked:
                Title_screen.button_pushed["Joystick up"] = True
                self.stick_locked = True
            elif event.value > DEADZONE and not self.stick_locked:
                Title_screen.button_pushed["Joystick down"] = True
                self.stick_locked = True
            elif -DEADZONE < event.value < DEADZONE:
                self.stick_locked = False

        elif event.type == pygame.JOYBUTTONDOWN and event.button == self.controller_buttons["A"]:
            Title_screen.button_pushed["Controller A"] = True

the_controller: Controller_Events = Controller_Events()

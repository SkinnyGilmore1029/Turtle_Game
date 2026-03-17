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
        self.cursor: Cursor = Cursor("Level 1")
        self.button_pushed: dict[int|str, bool] = {
            1: False,
            2: False,
            3: False,
            4: False,
            5: False,
            6: False,
            7: False,
            8: False,
            "Esc" : False
        }
        self.starting_pos:int = 200
        self.y_spacing:int = 40

    def choosing_level2(self, game: object) -> None:
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
                if key == "Esc":
                    game.game_state = "Title"
                else:
                    game.level = key
                    game.playing = True
                    game.game_state = "Playing"
                    player.rect.x, player.rect.y = level_positions[key]
                # Reset the button
                self.button_pushed[key] = False
                break

    def Title_Text(self, screen:pygame.Surface) -> None:
        """Yes this is mine"""
        Title = self.fonts["Title"].render("Choose Your Level!",True,"#F5E800")
        screen.blit(Title,(400,0))

    def explain_text(self, screen: pygame.Surface)-> None:
        pygame.draw.rect(screen,"Black", (680, 180, 510, 430), 20, 10, 10, 10, 10, 10)
        explain_text = self.fonts["Start Button"].render("Press the number of the level on the Keyboard to choose!",True,"#F5E800",None,500)
        control_text = self.fonts["Start Button"].render("Move the cursor to the level and press A",True,"#F5E800",None,400)
        back = self.fonts["Start Button"].render("Press the Escape button or the B button to go back to Title Screen",True,"#F5E800",None,500)
        screen.blits([
            (explain_text,(700,200)),
            (control_text,(700,350)),
            (back, (700, 500))
            ])

    def draw_option_text(self, screen: pygame.Surface) -> None:
        for i, _ in enumerate(range(8)):
            level = self.fonts["Start Button"].render(f"Level {i +1 }",True,"#F5E800")
            y_pos = self.starting_pos + i * self.y_spacing
            screen.blit(level,(self.starting_pos,y_pos))

    def draw_choose_level_screen2(self,screen: pygame.Surface)->None:
        screen.fill("Blue")
        self.explain_text(screen)
        self.Title_Text(screen)
        self.draw_option_text(screen)


Choosing_screen = Choose_Level('Title Screen')
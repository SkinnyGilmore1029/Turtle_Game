import pygame
from Level.Level_Creater import Level_Creater
from UI.Title_screen import Title_screen
from UI.Choosing_Screen import Choosing_screen
from UI.Cutscenes import Cut_scenes
from UI.Game_Over import Game_over_screen
from UI.Win_screen import Win
from Managers.Music_Manager import music
from Managers.Controller_Manager import the_controller
from Managers.KeyBoard_manager import the_keyboard
import sys
pygame.init()
pygame.joystick.init()



class Turtle_Game:
    def __init__(self):
        self.playing = False
        self.game_state = "Title"
        self.screen = pygame.display.get_surface()
        pygame.display.set_caption("Squartle's Quest")
        self.clock = pygame.time.Clock()
        self.level = 1
        self.room = 1
        self.current_level = Level_Creater(self.level,self.room)
        self.running: bool = True
        self.joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

    def handle_events(self):
        event_queue = pygame.event.get()

        for event in event_queue:
            if event.type == pygame.QUIT:
                self.running = False

            if event.type in (
                pygame.KEYDOWN,
                pygame.JOYBUTTONDOWN,
                pygame.KEYUP,
                pygame.JOYBUTTONUP,
                pygame.JOYHATMOTION,
                pygame.JOYAXISMOTION
                ):

                match self.game_state:
                    case "Choosing Level":
                        the_keyboard.handle_choosing_keyboard(event, self)
                    case "Playing":
                        the_controller.player_controller(event)

    def change_level(self):
        if (self.current_level.level != self.level):
            self.current_level.clear_level()
            self.current_level.The_Rooms.change_level(self.level)
            self.current_level.change_rooms(self.level, self.room)

    def change_level_room(self):
        if (self.current_level.room != self.room):
            self.current_level.change_rooms(self.level,self.room)



    def update_game(self,dt:float)->None:
        Game_over_screen.check_lives(self)
        self.change_level_room()
        self.change_level()
        self.current_level.update_level(dt,self)

    def draw(self):
        self.current_level.draw_level(self.screen,self)

    def Run(self)->None:
        while self.running:
            dt = self.clock.tick(60.0) / 1000
            self.handle_events()

            if not self.playing:
                music.stop_music()
                match self.game_state:
                    case "Title":
                        Title_screen.draw_Title_screen(self.screen)
                        Title_screen.Title_screen_controls(self)
                    case "Choosing Level":
                        Choosing_screen.draw_choose_level_screen2(self.screen)
                        Choosing_screen.choosing_level2(self)
                    case "Game Over":
                        Game_over_screen.draw_game_over_screen(self.screen)
                        Game_over_screen.game_over_controls(self)
                    case "Win Screen":
                        Win.draw(self.screen)
                        Win.controls(self)

            else:
                music.play_music("Music_Sounds/the-wandering-samurai-344699.mp3")
                match self.game_state:
                    case "Playing":
                        self.current_level.handle_collision_death(self)
                        self.current_level.handle_collision_winning(self)
                        self.update_game(dt)
                        self.draw()
                    case "Starting Cutscene":
                        Cut_scenes.update(dt,self)
                        Cut_scenes.draw(self.screen)


            pygame.display.flip()
        pygame.quit()
        sys.exit()

game = Turtle_Game()
if __name__ =="__main__":
    game.Run()

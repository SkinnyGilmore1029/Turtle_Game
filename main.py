import pygame
from Level.Level_Creater import Level_Creater
from UI.Title_screen import Title_screen
from UI.Choosing_Screen import Choosing_screen
from UI.Cutscenes import Cut_scenes
from UI.Game_Over import Game_over_screen
from UI.Win_screen import Win
from Utility.Music_Manger import music
import sys
pygame.init()

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
    
    def handle_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    def change_level(self):
        if (self.current_level.level != self.level):
            self.current_level.clear_level()
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
        while True:
            dt = self.clock.tick(60.0) / 1000
            self.handle_events()
            
            if self.playing is False:
                match self.game_state:
                    case "Title":
                        Title_screen.draw_Title_screen(self.screen)
                        Title_screen.Title_screen_controls(self)
                    case "Choosing Level":
                        Choosing_screen.draw_choose_level_screen(self.screen)
                        Choosing_screen.choosing_level(self)
                    case "Game Over":
                        Game_over_screen.draw_game_over_screen(self.screen)
                        Game_over_screen.game_over_controls(self)
                    case "Win Screen":
                        Win.draw(self.screen)
                        Win.controls(self)
                        
            if self.playing is True:
                music.play_music("Music_Sounds/the-wandering-samurai-344699.mp3")
                match self.game_state:
                    case "Playing":
                        self.current_level.handle_collision(self)
                        self.update_game(dt)
                        self.draw()
                    case "Starting Cutscene":
                        Cut_scenes.update(dt,self)
                        Cut_scenes.draw(self.screen)
                        
                
            pygame.display.flip()
            

if __name__ =="__main__":
    game = Turtle_Game()
    game.Run()

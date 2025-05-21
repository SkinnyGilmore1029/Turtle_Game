import pygame


class Screens:
    def __init__(self):
        self.fonts:dict = {
            "Title" : pygame.font.SysFont("Arial",48,True),
            "Start Button" : pygame.font.SysFont("Arial",32,True)
        }
     
    def begin_game(self,game):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            game.playing = True
            game.game_state = "Playing"
        
    def Title_screen_text(self,screen:pygame.Surface):
        Title = self.fonts["Title"].render("Squartle Quest!",True,"#F5E800")
        Start_button = self.fonts["Start Button"].render("Press S to start your quest!",True,"#F5E800")
        screen.blits([(Title,(240,40)),(Start_button,(100,640))])
        
    def draw_Title_screen(self,screen:pygame.Surface,game)->None:
        screen.fill("Blue")
        self.begin_game(game)
        self.Title_screen_text(screen)
        
Title_screen = Screens()
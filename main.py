import pygame
from Utility.Settings import WIDTH,HEIGHT
from The_turtles.The_player import player
from The_turtles.Jesse import jesse
from Levels.Level_Creater import Level_Creater
import sys

class Turtle_Game:
    Level_1 = Level_Creater(1,1)
    def __init__(self):
        self.playing = True
        self.screen = pygame.display.get_surface()
        pygame.display.set_caption("Turtle Game")
        self.clock = pygame.time.Clock()
        
    def Run(self)->None:
        while True:
            dt = self.clock.tick(60.0) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill("blue")
            self.Level_1.draw_level(self.screen)
            player.update(dt)
            jesse.update(dt)
            player.draw(self.screen)
            jesse.draw(self.screen)

            pygame.display.flip()
            

if __name__ =="__main__":
    game = Turtle_Game()
    game.Run()
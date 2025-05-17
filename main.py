import pygame
from Utility.Settings import WIDTH,HEIGHT
from Levels.Level_Creater import Level_Creater
import sys

class Turtle_Game:
    def __init__(self):
        self.playing = True
        self.screen = pygame.display.get_surface()
        pygame.display.set_caption("Turtle Game")
        self.clock = pygame.time.Clock()
        self.level = 1
        self.room = 1
        self.current_level = Level_Creater(self.level,self.room)
    
    def handle_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
    def update_game(self,dt:float)->None:
        self.change_level_dev()
        self.change_level()
        self.current_level.update_level(dt)
    
    def draw(self):
        self.current_level.draw_level(self.screen)
    
    def change_level_dev(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_2]:
            self.level = 2
        if keys[pygame.K_1]:
            self.level = 1
        if keys[pygame.K_t]:
            self.room = 2
        if keys[pygame.K_o]:
            self.room =1
            
    def change_level(self):
        if (self.current_level.level != self.level or
            self.current_level.room != self.room):
            self.current_level.change_background(self.level, self.room)
    
    def Run(self)->None:
        while True:
            dt = self.clock.tick(60.0) / 1000
            self.handle_events()
            if self.playing:
                self.update_game(dt)
                self.draw()
                
            pygame.display.flip()
            

if __name__ =="__main__":
    game = Turtle_Game()
    game.Run()
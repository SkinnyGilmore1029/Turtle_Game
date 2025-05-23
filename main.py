import pygame
from Level.Level_Creater import Level_Creater
from UI.Title_screen import Title_screen
from UI.Choosing_Screen import Choosing_screen
from UI.Cutscenes import Cut_scenes
import sys

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
        self.change_level_room()
        self.change_level()
        self.current_level.update_level(dt,self)
    
    def draw(self):
        self.current_level.draw_level(self.screen)
            
    def Run(self)->None:
        while True:
            dt = self.clock.tick(60.0) / 1000
            self.handle_events()
            
            if self.playing is False:
                match self.game_state:
                    case "Title":
                        Title_screen.draw_Title_screen(self.screen,self)
                    case "Choosing Level":
                        Choosing_screen.draw_choose_level_screen(self.screen)
                        Choosing_screen.choosing_level(self)
                    case "Game Over":
                        pass
            
            if self.playing is True:
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
    
    
"""
    turtle 1 calls this
  def move_turtle3(self) -> pygame.Rect:
        if self.direction == 'down':
            self.rect.y += 6
            if self.rect.y > HEIGHT +self.w:
                self.unload()
                self.begging = True

    turtle 2 calls this
    def move_turtle2(self) -> pygame.Rect:
        if self.direction == 'down':
            self.rect.y += 5
            if self.rect.y >= HEIGHT + self.w:
                self.unload()
                All_turtles['turtle1'].direction = 'down'
                
    def starting_cut_scene(self,screen:pygame.Surface):
        if BGF.All_levels['level count'].level == 0:
            bg = pygame.image.load(join("Other Pictures","title bg.png")).convert()
            screen.blit(bg,(0,0))
            TGG.All_turtles['turtle1'].draw(screen)
            TGG.All_turtles['turtle2'].draw(screen)
            TGG.All_turtles['turtle2'].move_turtle2()
            TGG.All_turtles['turtle1'].move_turtle3()
            BG.All_Badguys['starting villain'].cutscene_1(screen,TGG.All_turtles['turtle2']) 
            if TGG.All_turtles['turtle2'].direction == 'up':
                chilling = All_fonts['Title_font'].render("While these turtles are just chilling..",True,"black","white")
                chilling_rect = chilling.get_rect(topleft=(0,0))
                screen.blit(chilling,chilling_rect)
            elif TGG.All_turtles['turtle2'].direction == 'down':
                taken = All_fonts['Title_font2'].render("This guy kidnapped the Green Turtle's friend",True,"black","white")
                taken_rect = taken.get_rect(topleft=(0,0))
                screen.blit(taken,taken_rect)
            if TGG.All_turtles['turtle1'].direction == 'down':
                begin = All_fonts['Title_font2'].render("Now begins his journey to save his friend!",True,"black","white")
                begin_rect = begin.get_rect(topleft=(0,0))
                screen.blit(begin,begin_rect)
            if TGG.All_turtles['turtle1'].begging is True:
                BGF.All_levels['level count'].level = 1
                
"""
import pygame
from Utility.Settings import WIDTH


level_font = pygame.font.SysFont("Arial",20,True)

def Show_hud(screen,player,level,room):
    lives = level_font.render(f"Lives: {player.lives}",True,"black","green",150)
    keys = level_font.render(f"Keys: {player.key_count}",True,"black","green",150)
    on_level = level_font.render(f"Level: {level}",True,"black","green",150)
    in_room = level_font.render(f"Room: {room}",True,"black","green",150)
    screen.blits([(lives,(0,0)),(keys,(0,20)),(on_level,(WIDTH-100,0)),(in_room,(WIDTH-100,20))])
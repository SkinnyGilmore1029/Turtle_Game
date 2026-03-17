import pygame
from Managers.Image_Manager import my_image
from Managers.Data_Manager import data

class Room2_Arrow(pygame.sprite.Sprite):
    def __init__(self, name:str, level:int, x:int, y:int):
        super().__init__()
        self.name = name
        self.level = level
        self.x = x
        self.y = y
        self.image = my_image.load_image(self.name)
        self.image = pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect()

    def draw(self, screen:pygame.Surface) -> None:
        screen.blit(self.image,(self.x,self.y))

class Room2_Arrow_Group(pygame.sprite.GroupSingle):
    def __init__(self):
        super().__init__()

    def get_arrows(self, level:int, room:int) -> None:
        self.empty()
        arrow_data = data.load_level_data(level, "arrow")
        for a in arrow_data.values():
            if a['room'] == room:
                arrow = self.create_arrows(a)
                self.add(arrow)

    def create_arrows(self, data:dict) -> Room2_Arrow:
        return Room2_Arrow(
            name= data["name"],
            level= data["level"],
            x= data["x"],
            y= data["y"]
        )

    def draw(self, screen:pygame.Surface) -> None:
        for sprite in self:
            sprite.draw(screen)

Room2_arrow = Room2_Arrow_Group()
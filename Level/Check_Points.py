import pygame
from The_turtles.The_player import player
from Managers.Data_Manager import data

class CheckPoint(pygame.sprite.Sprite):
    def __init__(self, x:int, y:int, width:int, height:int, acquired:bool, level:int, save_key:str, color:str):
        super().__init__()
        self.name = "Check Points"
        self.x:int = x
        self.y:int = y
        self.w:int = width
        self.h:int = height
        self.save_key:str = save_key
        self.color:str = color
        self.rect: pygame.Rect = pygame.Rect(self.x,self.y,self.w,self.h)
        self.acquired: bool = acquired
        self.level: int = level
        self.room:int = 2
        self.visible:bool = False

    def get_check_point(self) -> None:
        """Responsible for checking collision with
        player and switching self.acquired to True if
        it is False.
        """
        if pygame.sprite.collide_rect(self, player) and self.visible:
            self.acquired = True
            self.color = "#30AD17"


    def update(self, game:object) -> None:
        self.get_check_point()
        if game.room == 2:
            self.visible = True
        else:
            self.visible = False

    def draw(self, screen:pygame.Surface) -> None:
        if self.visible:
            pygame.draw.rect(screen,self.color,self.rect)

class CheckPointGroup(pygame.sprite.GroupSingle):
    def __init__(self):
        super().__init__()
        self.got_check_point:set[str] = set()

    def get_check_data(self, level:int)-> None:
        self.empty()
        cp_data = data.load_level_data(level,"checkpoints")
        for cp in cp_data.values():
            TheCheckPoint = self.make_check_point(cp)
            self.add(TheCheckPoint)

    def empty_cp(self) -> None:
        self.empty()
        self.got_check_point.clear()

    def make_check_point(self, data:dict) -> CheckPoint:
        return CheckPoint(
            x= data['x'],
            y= data["y"],
            width= data["width"],
            height= data["height"],
            acquired= data["acquired"],
            level= data["level"],
            save_key= data["save key"],
            color= data['color']
        )

    def update(self, game:object) -> None:
        if self.sprite:
            self.sprite.update(game)
            if self.sprite.acquired == True and self.sprite.save_key not in self.got_check_point:
                self.got_check_point.add(self.sprite.save_key)
            if self.sprite.save_key in self.got_check_point:
                self.sprite.acquired = True
                self.sprite.color = "#30AD17"


    def draw(self, screen: pygame.Surface) -> None:
        if self.sprite:
            self.sprite.draw(screen)

Check_point: CheckPointGroup = CheckPointGroup()
import pygame
from Utility.Image_Handler import Image_Animator,data
from Utility.Settings import WIDTH,HEIGHT

class Teleporter(pygame.sprite.Sprite):
    def __init__(self, name:str, x:float, y:float, width:int, height:int, frame_count:int)->None:
        super().__init__()
        self.name = name
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        self.sheet_size:list[int,int] = [520,128]
        self.rect = pygame.FRect(self.x, self.y, self.w, self.h)
        self.frame_count = frame_count

        # Use your animator class
        self.animator = Image_Animator(self.name, change_time=150)
        self.animator.load_frames(self.name, self.frame_count, self.w, self.h,self.sheet_size)

        self.image = self.animator.frames[0]
        self.mask = pygame.mask.from_surface(self.image)

    

    def update(self):
        self.image = self.animator.play(self.frame_count)
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, screen:pygame.Surface)->None:
        screen.blit(self.image, self.rect)


class Tele_Group(pygame.sprite.GroupSingle):
    def __init__(self):
        super().__init__()
        
    def get_tele_data(self,level:int,room:int)->None:
        self.empty()
        tele_data = data.load_level_teleporter(level)
        for t in tele_data.values():
            if t['in_room'] == room:
                teleporter = self.create_teleporter(t)
                self.add(teleporter)
                
    def create_teleporter(self,data:dict):
        return Teleporter(
            name= data["name"],
            x= data['x'],
            y= data['y'],
            width= data['width'],
            height = data['height'],
            frame_count= data['frame_count']
        )

    def collision_with_player(self,player:object):
        if self.sprite:
            if pygame.sprite.collide_mask(self.sprite,player):
                self.remove(self.sprite)
                return True
            return False

    def update(self):
        if self.sprite:
            self.sprite.update()
            
    def draw(self,screen):
        if self.sprite:
            self.sprite.draw(screen)
            
The_tele = Tele_Group()
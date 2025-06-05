import pygame
from Utility.Image_Handler import data


class Lock(pygame.sprite.Sprite):
    def __init__(self,name:str,x:float,y:float,width:int,height:int):
        super().__init__()
        self.name = name
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        self.image = data.load_image(name)
        self.image = pygame.transform.smoothscale(self.image,(self.w,self.h))
        self.rect = pygame.FRect(self.x,self.y,self.w,self.h)
        self.mask = pygame.mask.from_surface(self.image)
        self.locked = True
        self.can_unlock = False

    def lock_collision(self,player)->None:
        if pygame.sprite.collide_mask(self,player):
            if player.key_count < 1:
                if player.rect.top <= self.rect.top:
                    player.rect.bottom = self.rect.top
                elif player.rect.bottom >= self.rect.bottom:
                    player.rect.top = self.rect.bottom
                elif player.rect.right < self.rect.right:
                    player.rect.right = self.rect.left
                elif player.rect.left > self.rect.left:
                    player.rect.left = self.rect.right
            elif player.key_count >= 1:
                self.can_unlock = True
                player.key_count -=1

    def unlock(self)->None:
        if self.can_unlock == True:
            self.locked = False

    def update(self,player):
        self.lock_collision(player)
        self.unlock()

    def draw(self,screen:pygame.Surface)->None:
        screen.blit(self.image,self.rect)
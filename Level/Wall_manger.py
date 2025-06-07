import pygame
from Utility.Image_Handler import data
from NPCS.The_crabs import The_Crabs
from The_turtles.The_player import player
from Enemy.The_Enemy_Group import bad_guys
from .Buttons import Button_group
from .Locks_Group import the_lock


class The_Walls(pygame.sprite.Sprite):
    def __init__(self,name:str,x:float,y:float,width:float,height:float,direction:str,room:int)->None:
        super().__init__()
        self.name = name
        self.image = data.load_image(name)
        self.ignore = ["Bolder","Tornado","Fish"]
        self.wall_id = ""
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.room = room
        self.direction = direction
        self.handle_wall_direction()
        self.rect = pygame.FRect(self.x,self.y,self.width,self.height)
        self.mask = pygame.mask.from_surface(self.image)

    def handle_wall_direction(self):
        match self.direction:
            case "top":
                self.image = pygame.transform.smoothscale(self.image,(self.width,self.height))
            case "bottom":
                self.image = pygame.transform.smoothscale(self.image,(self.width,self.height))
                self.image = pygame.transform.flip(self.image,False,True)
            case "left":
                self.image = pygame.transform.rotate(self.image, -90.0)
                self.image = pygame.transform.flip(self.image, True, False)
                self.image = pygame.transform.smoothscale(self.image, (self.width, self.height))
            case 'right':
                self.image = pygame.transform.rotate(self.image, -90.0)
                self.image = pygame.transform.smoothscale(self.image, (self.width, self.height))
        self.mask = pygame.mask.from_surface(self.image)

    def wall_collision(self) -> None:
        if pygame.sprite.collide_mask(self,player):
            if player.rect.top <= self.rect.top:
                player.rect.bottom = self.rect.top
            elif player.rect.bottom >= self.rect.bottom:
                player.rect.top = self.rect.bottom
            elif player.rect.right < self.rect.right:
                player.rect.right = self.rect.left
            elif player.rect.left > self.rect.left:
                player.rect.left = self.rect.right

    def enemy_collision(self) -> None:
        for e in bad_guys:
            if self.rect.colliderect(e.rect) and e.name not in self.ignore:
                dx_left = abs(self.rect.left - e.rect.right)
                dx_right = abs(self.rect.right - e.rect.left)
                dy_top = abs(self.rect.top - e.rect.bottom)
                dy_bottom = abs(self.rect.bottom - e.rect.top)

                min_dist = min(dx_left, dx_right, dy_top, dy_bottom)

                if min_dist == dy_top:
                    # hit from top
                    e.rect.bottom = self.rect.top
                    e.velocity.y *= -1
                    e.direction = 'Down'
                elif min_dist == dy_bottom:
                    # hit from bottom
                    e.rect.top = self.rect.bottom
                    e.velocity.y *= -1
                    e.direction = 'Up'
                elif min_dist == dx_left:
                    # hit from left
                    e.rect.right = self.rect.left
                    e.velocity.x *= -1
                    e.direction = 'Right'
                elif min_dist == dx_right:
                    # hit from right
                    e.rect.left = self.rect.right
                    e.velocity.x *= -1
                    e.direction = 'Left'

    def update(self,dt)->None:
        self.wall_collision()
        self.enemy_collision()

    def draw(self,screen):
        screen.blit(self.image,self.rect)
        
class The_vines(The_Walls):
    def __init__(self,name:str,x:float,y:float,width:float,height:float,direction:str,room:int):
        super().__init__(name,x,y,width,height,direction,room)
        self.despawn:bool = False
        self.cut:bool = False
        self.pos:tuple[int,int] = (self.x,self.y)
        
    def cut_vine(self):
        for crab in The_Crabs:
            if pygame.sprite.collide_mask(self,crab):
                self.cut = True
    
    def move(self,dt)->None:
        if self.cut == True:
            match self.direction:
                case "top":
                    self.rect.y -= 150 * dt
                    if self.rect.y <= 0 - self.height:
                        self.despawn = True
                case "bottom":
                    self.rect.y += 150 * dt
                    if self.rect.y >= 800:
                        self.despawn = True
                    
    def update(self,dt):
        self.wall_collision()
        self.cut_vine()
        self.move(dt)
        

class Cage_Doors(The_Walls):
    def __init__(self,name:str,x:float,y:float,width:float,height:float,direction:str,room:int):
        super().__init__(name,x,y,width,height,direction,room)
        self.can_move:bool = False
        self.can_unlock: bool = False
        self.pos:tuple[int,int] = (self.x,self.y)
        self.speed = 100
        
    def check_buttons(self):
        for button in Button_group:
            if button.name2 == self.wall_id and button.pressed:
                self.can_move = True
    
    def check_lock(self):
        if the_lock.sprite is None:
            self.can_unlock = True
    
    def move_cages(self,dt:float):
        if self.can_move:
            match self.wall_id:
                case "Button4":
                    self.rect.x += self.speed *dt
                    if self.rect.x >= self.pos[0] + self.width:
                        self.speed = 0
                case "Button3":
                    self.rect.x -= self.speed * dt
                    if self.rect.x <= self.pos[0] - self.width:
                        self.speed = 0
                case "Button1":
                    self.rect.x += self.speed * dt
                    if self.rect.x >= self.pos[0] + self.width:
                        self.speed = 0
                case "Button2":
                    self.rect.y -= self.speed * dt
                    if self.rect.y <= self.pos[1] - self.height:
                        self.speed = 0
    
    def unlock_doors(self,dt:float):
        if self.can_unlock:
            match self.wall_id:
                case "Lock Top":
                    self.rect.y -= self.speed *dt
                    if self.rect.y <= self.pos[1] - self.height:
                        self.speed = 0
                case "Lock Bottom":
                    self.rect.y += self.speed *dt
                    if self.rect.y >= self.pos[1] + self.height:
                        self.speed = 0
    
    def update(self,dt):
        self.check_lock()
        self.check_buttons()
        self.wall_collision()
        self.enemy_collision()
        self.move_cages(dt)
        self.unlock_doors(dt)

        
class The_walls_group(pygame.sprite.Group):
    wall_classes:dict = {
        "Fence" : The_Walls,
        "Rock Wall" : The_Walls,
        "Desert" : The_Walls,
        "Desert2" : The_Walls,
        "Vine" : The_vines,
        "Cliffs" : The_Walls,
        "Fort Wall" : The_Walls,
        "Cage Front" : Cage_Doors,
        "Cage Gate" :  Cage_Doors,
        "Fort Top" : The_Walls
    }
    def __init__(self):
        super().__init__()
        self.loaded_room = set()
        self.moved_walls = set()
        
    def load_group(self,level:int,room:int)->None:
        self.empty()
        key = (level,room)
        
        if key not in self.loaded_room:
            walls = data.load_level_data(level,"walls")
            
            for w in walls.values():
                cut_key = (w['name'],w['direction'],w['x'])
                
                if w['room'] == room and cut_key not in self.moved_walls:
                    wall = self.create_walls(w)
                    wall.wall_id = w['level']
                    self.add(wall)
                  
            self.loaded_room.add(key)
    
    def create_walls(self,data:dict)->None:
        clas = self.wall_classes.get(data["name"])
        if clas:
            return clas(
                name= data["name"],
                x= data['x'],
                y= data['y'],
                width= data['width'],
                height= data['height'],
                direction= data['direction'],
                room= data['room'])


    def check_if_vine(self,sprite)->None:
        if isinstance(sprite,The_vines):
                cut_key = (sprite.name,sprite.direction,sprite.x)
                if sprite.despawn:
                    self.moved_walls.add(cut_key)
                    self.remove(sprite)

    def update(self,dt):
        for sprite in list(self):
            self.check_if_vine(sprite)
            sprite.update(dt)
    
    def change_room(self):
        self.empty()
        self.loaded_room.clear()
        
    
    def draw(self,screen:pygame.Surface)->None:
        for sprite in self:
            sprite.draw(screen)
            
All_walls = The_walls_group()
import pygame
from Utility.Image_Handler import data
from NPCS.The_crabs import The_Crabs

class The_Walls(pygame.sprite.Sprite):
    def __init__(self,name:str,x:float,y:float,width:float,height:float,direction:str,room:int)->None:
        super().__init__()
        self.image = data.load_image(name)
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

    def wall_collision(self,josh) -> None:
        if pygame.sprite.collide_mask(self,josh):
            if josh.rect.top <= self.rect.top:
                josh.rect.bottom = self.rect.top
            elif josh.rect.bottom >= self.rect.bottom:
                josh.rect.top = self.rect.bottom
            elif josh.rect.right < self.rect.right:
                josh.rect.right = self.rect.left
            elif josh.rect.left > self.rect.left:
                josh.rect.left = self.rect.right

    def draw(self,screen,josh):
        self.wall_collision(josh)
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
                        self.rect.y = 0 -self.height
                case "bottom":
                    self.rect.y += 150 * dt
                    if self.rect.y >= 800 + self.height:
                        self.despawn = True 
                        self.rect.y = 800 + self.height
                    
    def update(self,dt):
        self.cut_vine()
        self.move(dt)
        
        
class The_walls_group(pygame.sprite.Group):
    wall_classes:dict = {
        "Fence" : The_Walls,
        "Rock Wall" : The_Walls,
        "Vine" : The_vines
    }
    def __init__(self):
        super().__init__()
        self.loaded_room = set()
        
    def load_group(self,level:int,room:int)->None:
        key = (level,room)
        if key not in self.loaded_room:
            walls = data.load_level_data(level,"walls")
            #walls = data.load_wall_data(level)
            for w in walls.values():
                if w['room'] == room:
                    wall = self.create_walls(w)
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


    def update(self,dt):
        for sprite in list(self):
            if isinstance(sprite,The_vines):
                if sprite.despawn == True:
                    self.remove(sprite)
                    print("vine despawned")
                sprite.update(dt)
    
    def change_room(self):
        self.empty()
        self.loaded_room.clear()
        
    
    def draw(self,screen:pygame.Surface,josh)->None:
        for sprite in self:
            sprite.draw(screen,josh)
            
All_walls = The_walls_group()
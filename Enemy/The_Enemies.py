import pygame
from Utility.Settings import WIDTH,HEIGHT
from Utility.Image_Handler import Image_Animator, data


class Bad_guy(pygame.sprite.Sprite):
    """
    This is a parent Class for all the rest of
    the class that can kill the player.
    """
    def __init__(self,name:str,x:float,y:float,width:int,height:int,direction:str,frame_count:int,in_room:int,speed:list)->None:
        super().__init__()
        self.name = name
        self.x = x 
        self.y = y
        self.w = width
        self.h = height
        self.in_room = in_room
        self.rect = pygame.FRect(self.x,self.y,self.w,self.h)
        self.direction = direction
        self.speed:list[int,int] = speed
        self.velocity = pygame.Vector2(speed[0],speed[1])
        self.frame_count = frame_count
        self.frames = data.get_frames(self.name,self.frame_count,self.w,self.h)
        self.animation = Image_Animator(self.name)
        self.transformed_frames = {
            "Left": [],
            "Right": [],
            "Up" : []
        }
        self.pre_load_frames()
        self.current_frame = 0
        self.image = self.transformed_frames[self.direction][self.current_frame]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_timer = pygame.time.get_ticks()
        self.animation_speed = 200  # ms per frame
        
    def pre_load_frames(self):
        """
        Prepares and transforms the player's animation frames for each facing direction.

        This method iterates through the original frames, performing transformations to 
        produce separate frame lists for 'Up', 'Down', 'Left', and 'Right' directions:
            - 'Left': Rotates the image -90 degrees, flips it horizontally, and scales it.
            - 'Right': Rotates the image -90 degrees and scales it.

        The resulting frames are stored in the `transformed_frames` dictionary 
        keyed by direction.
        """
        for frame in self.frames:
            up_img = pygame.transform.smoothscale(frame, (self.w, self.h))
            self.transformed_frames["Up"].append(up_img)
            
            left_img = pygame.transform.flip(frame, True, False)
            left_img = pygame.transform.smoothscale(left_img, (self.w, self.h))
            self.transformed_frames["Left"].append(left_img)
            
            right_img = pygame.transform.smoothscale(frame, (self.w, self.h))
            self.transformed_frames["Right"].append(right_img)
            
    def handle_animations(self)->None:
        """
        Handles player animation frame updates based on elapsed time.

        Advances the animation frame if enough time has passed, and updates 
        the current image and collision mask based on the facing direction.
        """

         # Animate frames over time
        current_time = pygame.time.get_ticks()
        if current_time - self.animation_timer > self.animation_speed:
            self.current_frame = (self.current_frame + 1) % self.frame_count
            self.animation_timer = current_time
        
        # Set current image to the correct frame and direction (no transforms here)
        self.image = self.transformed_frames[self.direction][self.current_frame]
        self.mask = pygame.mask.from_surface(self.image)
 
    def move(self,dt:float)->None:
        #childern class will complete
        pass
        
    def update(self):
        #childern class will complete
        pass
        
    def draw(self,screen:pygame.Surface)->None:
        #childern class will complete
        pass

class The_cars(Bad_guy):
    def __init__(self,name:str,x:float,y:float,width:int,height:int,direction:str,frame_count:int,in_room:int,speed:list)->None:
        super().__init__(name,x,y,width,height,direction,frame_count,in_room,speed)

    def move(self,dt:float)->None:
        self.rect.x -=self.velocity.x *dt
        if self.rect.x < -128:
            self.rect.x = WIDTH + 30

    def update(self,dt):
        self.move(dt)
        self.handle_animations()
        
    def draw(self,screen:pygame.Surface)->None:
        screen.blit(self.image,self.rect)

class The_trucks(Bad_guy):
    def __init__(self,name:str,x:float,y:float,width:int,height:int,direction:str,frame_count:int,in_room:int,speed:list)->None:
        super().__init__(name,x,y,width,height,direction,frame_count,in_room,speed)
    
    def move(self,dt:float)->None:
        self.rect.x -=self.velocity.x *dt
        if self.rect.x > WIDTH+50:
            self.rect.x = -50

    def update(self,dt):
        self.move(dt)
        self.handle_animations()
        
    def draw(self,screen:pygame.Surface)->None:
        screen.blit(self.image,self.rect)
        
class The_bus(Bad_guy):
    def __init__(self,name:str,x:float,y:float,width:int,height:int,direction:str,frame_count:int,in_room:int,speed:list)->None:
        super().__init__(name,x,y,width,height,direction,frame_count,in_room,speed)
        
    def move(self,dt:float)->None:
        self.rect.x -=self.velocity.x *dt
        if self.rect.x < -128:
            self.rect.x = WIDTH + 30

    def update(self,dt):
        self.move(dt)
        self.handle_animations()
        
    def draw(self,screen:pygame.Surface)->None:
        screen.blit(self.image,self.rect)
        
class The_gators(Bad_guy):
    def __init__(self,name:str,x:float,y:float,width:int,height:int,direction:str,frame_count:int,in_room:int,speed:list)->None:
        super().__init__(name,x,y,width,height,direction,frame_count,in_room,speed)
    
    def move_up_down(self, dt: float) -> None:
        self.rect.y += self.velocity.y * dt

        if self.rect.y <= 150:
            self.rect.y = 150
            self.velocity.y *= -1

        elif self.rect.y >= 500:
            self.rect.y = 500
            self.velocity.y *= -1
    
    def move_left_right(self, dt: float) -> None:
        self.rect.x += self.velocity.x * dt

        if self.rect.x <= 0:
            self.rect.x = 0
            self.velocity.x *= -1
            match self.direction:
                case "Left":
                    self.direction = "Right"
                case "Right":
                    self.direction = "Left"

        elif self.rect.x >= WIDTH - self.w:
            self.rect.x = WIDTH - self.w
            self.velocity.x *= -1
            match self.direction:
                case "Left":
                    self.direction = "Right"
                case "Right":
                    self.direction = "Left"

        
    def move(self,dt:float)->None:
        self.move_left_right(dt)
        self.move_up_down(dt)
    
    def update(self,dt:float)->None:
        self.move(dt)
        self.handle_animations()
        
    def draw(self,screen:pygame.Surface)->None:
        screen.blit(self.image,self.rect)
        
class Main_Boss(Bad_guy):
    def __init__(self,name:str,x:float,y:float,width:int,height:int,direction:str,frame_count:int,in_room:int,speed:list)->None:
        super().__init__(name,x,y,width,height,direction,frame_count,in_room,speed)
    
    def get_single_image(self):
        return data.load_image(self.name)
    
    def get_turtle(self,turtle:object,dt:float):
        self.rect.y -= self.speed[1] *dt
        if pygame.sprite.collide_mask(self, turtle):
            self.rect.y += self.speed[1] *dt
            turtle.rect.y += self.speed[1]*dt
        if self.rect.y > HEIGHT:
            self.rect.y = HEIGHT
        
    def draw_cutscene1(self,screen:pygame.Surface)->None:
        self.image = self.get_single_image()
        self.mask = pygame.mask.from_surface(self.image)
        screen.blit(self.image,self.rect)
        
    def draw_animated(self,screen:pygame.Surface)->None:
        screen.blit(self.image,self.rect)
        
boss = Main_Boss("Boss",472,700,96,96,"Up",4,1,[150,150])
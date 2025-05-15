import json
import pygame

_cached_image_data = {}

def get_image_data(Key:str,path:str)->dict:
    """This function just loads
    the json file to get image
    locations for join.

    Args:
        Key (str): The key of the dictionary in
        the json file.

    Returns:
        dict: The dictionary of image paths
    """
    if Key not in _cached_image_data:
        with open(path,'r') as f:
            images = json.load(f)
            image_paths = images[Key]
            _cached_image_data[Key] = image_paths
    return _cached_image_data[Key]

#cached images to make sure they dont reload
_loaded_images = {}

def load_image(picture_name:str)->pygame.Surface:
    """This function loads the picture
    from the specified path or the Error
    image if the picture doesn't exist.

    Args:
        picture_name (str): The name of the picture to load

    Returns:
        pygame.Surface: The image on a pygame.Surface that can be used with pygame.Rectangles
    """
    if picture_name not in _loaded_images:
        try:
            image = pygame.image.load(single_pictures[picture_name]).convert_alpha()
        except KeyError:
            image_surface = pygame.Surface((128,128),pygame.SRCALPHA).convert_alpha()
            image_surface.fill((255,0,0))
            image = image_surface
        _loaded_images[picture_name] = image
    return _loaded_images[picture_name]

def load_sheet(sheet_name:str)->pygame.Surface:
    """This function loads the picture
    from the specified path or the Error
    image if the picture doesn't exist.

    Args:
        picture_name (str): The name of the picture to load

    Returns:
        pygame.Surface: The image on a pygame.Surface that can be used with pygame.Rectangles
    """
    if sheet_name not in _loaded_images:
        try:
            image = pygame.image.load(sheets[sheet_name]).convert_alpha()
        except KeyError:
            image_surface = pygame.Surface((128,128),pygame.SRCALPHA).convert_alpha()
            image_surface.fill((255,0,0))
            image = image_surface
        _loaded_images[sheet_name] = image
    return _loaded_images[sheet_name]

_loaded_frames = {}

class Image_Animator:
    def __init__(self,name:str,frame:int = 0, change_time:int = 200)-> None:
        self.name = name
        self.frame = frame
        self.change_time = change_time
        self.start_time = pygame.time.get_ticks()
        self.frames:list[pygame.Surface] = []
        
    def get_image(self,name:str,frame:int,width:int,height:int)->pygame.Surface:
        sheet = load_sheet(name)
        image = pygame.Surface((width,height),pygame.SRCALPHA)
        image.blit(sheet,(0,0),(frame * width, 0, width, height))
        return image
    
    def load_frames(self,name:str,frame_count:int,width:int,height:int)->None:
        self.frames = [self.get_image(name,i,width,height) for i in range(frame_count)]
        
    def play(self,frame_count:int)->pygame.Surface:
        current_time = pygame.time.get_ticks()
        if (current_time - self.start_time) > self.change_time:
            self.frame = (self.frame + 1) % frame_count
            self.start_time = current_time
        return self.frames[self.frame]


def get_frames(name, frame_count, w, h):
    key = (name, frame_count, w, h)
    if key not in _loaded_frames:
        animator = Image_Animator(name)
        animator.load_frames(name, frame_count, w, h)
        _loaded_frames[key] = animator.frames
    return _loaded_frames[key]

#Normal Dictionary for load_image()
single_pictures = get_image_data("Normal","Utility/Sprites_Data.json")
sheets = get_image_data("Sheets","Utility/Sprites_Data.json")

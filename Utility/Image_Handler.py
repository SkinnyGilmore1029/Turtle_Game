import json
import pygame

#cached images to make sure they dont reload
_cached_image_data = {}
_loaded_images = {}
_loaded_frames = {}
_cached_level_data = {}

#functions to help load the json data
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

def load_sheet_data(sheet_name:str)->pygame.Surface:
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

def load_level_room_data(level_num: int, path: str) -> dict:
    if path not in _cached_level_data:
        with open(path, 'r') as f:
            _cached_level_data[path] = json.load(f)
    full_dict = _cached_level_data[path]
    level_key = f"Level {level_num}"
    level_backgrounds = full_dict[level_key]
    return level_backgrounds["Background"]

def load_level_background(level_num: int, room_num: float) -> pygame.Surface:
    room_key = f"Room {room_num}"
    room_bg = load_level_room_data(level_num, "Utility/Image json/Level_data.json")
    room_image_path = room_bg[room_key]
    try:
        level_background = pygame.image.load(room_image_path).convert_alpha()
    except (KeyError, FileNotFoundError):
        # Return a placeholder surface if image loading fails
        image_surface = pygame.Surface((1200, 800), pygame.SRCALPHA).convert_alpha()
        image_surface.fill((255, 50, 125))
        level_background = image_surface
    return level_background


def get_frames(name:str, frame_count:int, w:int, h:int)->list[pygame.Surface]:
    key = (name, frame_count, w, h)
    if key not in _loaded_frames:
        animator = Image_Animator(name)
        animator.load_frames(name, frame_count, w, h)
        _loaded_frames[key] = animator.frames
    return _loaded_frames[key]

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


class Image_Animator:
    def __init__(self,name:str,frame:int = 0, change_time:int = 200)-> None:
        self.name = name
        self.frame = frame
        self.change_time = change_time
        self.start_time = pygame.time.get_ticks()
        self.frames:list[pygame.Surface] = []
        
    def get_image(self,name:str,frame:int,width:int,height:int)->pygame.Surface:
        sheet = load_sheet_data(name)
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


#Normal Dictionary for load_image()
single_pictures = get_image_data("Normal","Utility/Image json/Sprites_Data.json")
sheets = get_image_data("Sheets","Utility/Image json/Sprites_Data.json")


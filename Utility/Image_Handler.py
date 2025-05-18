import json
import pygame

#cached images to make sure they dont reload
_cached_image_data = {}

#functions to help load the json data
#functions for Sprites_Data.json
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

class Image_Animator:
    def __init__(self,name:str,frame:int = 0, change_time:int = 200)-> None:
        self.name = name
        self.frame = frame
        self.change_time = change_time
        self.start_time = pygame.time.get_ticks()
        self.frames:list[pygame.Surface] = []
        
    def get_image(self,name:str,frame:int,width:int,height:int)->pygame.Surface:
        sheet = data.load_sheet_data(name)
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

class DataManager:
    def __init__(self):
        self._cached_level_data = {}
        self._cached_image_data = {}
        self._loaded_images = {}
        self._loaded_frames = {}
        self.sheets = get_image_data("Sheets", "Utility/JSON Data/Sprites_Data.json")
        self.single_pictures = get_image_data("Normal", "Utility/JSON Data/Sprites_Data.json")

    def _load_json_file(self, path: str) -> dict:
        if path not in self._cached_level_data:
            with open(path, 'r') as f:
                self._cached_level_data[path] = json.load(f)
        return self._cached_level_data[path]

    def load_level_background_data(self, level_num: int) -> dict[str, str]:
        path = f"Utility/JSON Data/Level{level_num}/Level{level_num}_background.json"
        return self._load_json_file(path)

    def load_level_enemies_data(self, level_num: int) -> dict[str, dict]:
        path = f"Utility/JSON Data/Level{level_num}/Level{level_num}_enemies.json"
        return self._load_json_file(path)

    def load_sheet_data(self, sheet_name: str) -> pygame.Surface:
        if sheet_name not in self._loaded_images:
            try:
                image = pygame.image.load(self.sheets[sheet_name]).convert_alpha()
            except (KeyError, FileNotFoundError):
                image = pygame.Surface((128, 128), pygame.SRCALPHA)
                image.fill((255, 0, 0))
            self._loaded_images[sheet_name] = image
        return self._loaded_images[sheet_name]

    def load_image(self, picture_name: str) -> pygame.Surface:
        if picture_name not in self._loaded_images:
            try:
                image = pygame.image.load(self.single_pictures[picture_name]).convert_alpha()
            except (KeyError, FileNotFoundError):
                image = pygame.Surface((128, 128), pygame.SRCALPHA)
                image.fill((255, 0, 0))
            self._loaded_images[picture_name] = image
        return self._loaded_images[picture_name]

    def get_frames(self, name: str, frame_count: int, w: int, h: int) -> list[pygame.Surface]:
        key = (name, frame_count, w, h)
        if key not in self._loaded_frames:
            animator = Image_Animator(name)
            animator.load_frames(name, frame_count, w, h)
            self._loaded_frames[key] = animator.frames
        return self._loaded_frames[key]

    def load_background_image(self, level_num: int, room: int) -> pygame.Surface:
        room_key = f"Room {room}"
        room_data = self.load_level_background_data(level_num)
        image_string = room_data["Background"][room_key]
        try:
            background_image = pygame.image.load(image_string).convert_alpha()
        except (KeyError, FileNotFoundError):
            background_image = pygame.Surface((1200, 800), pygame.SRCALPHA)
            background_image.fill((255, 50, 125))
        return background_image

# Initialize the data manager once:
data = DataManager()



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

#Normal Dictionary for load_image()
single_pictures = get_image_data("Normal","Utility/Sprites_Data.json")
import json
import pygame
import pygame.surfarray
import numpy as np
from pathlib import Path
import sys
import pygame
from Managers.Data_Manager import json_handler, data

if getattr(sys, 'frozen', False):  # PyInstaller exe
    PROJECT_ROOT = Path(sys._MEIPASS)  # PyInstaller temp folder
else:
    PROJECT_ROOT = Path(__file__).resolve().parent.parent


JSON_DATA_DIR = PROJECT_ROOT / "Utility"/ "JSON Data"
IMAGE_DATA = JSON_DATA_DIR / "Sprites_Data.json"


class Image_Handler:
    def __init__(self):
        self._loaded_images = {}

    def load_image(self, picture_name: str) -> pygame.Surface:
        if picture_name not in self._loaded_images:
            try:
                image = pygame.image.load(json_handler._load_json_file(IMAGE_DATA)["Normal"][picture_name]).convert_alpha()
                arr = pygame.surfarray.pixels3d(image)
                alpha_arr = pygame.surfarray.pixels_alpha(image)

                # Find white pixels (255,255,255)
                white_mask = np.all(arr == [255, 255, 255], axis=-1)
                alpha_arr[white_mask] = 0  # Set alpha to 0 where white

                del arr  # Unlock surface
                del alpha_arr

            except (KeyError, FileNotFoundError):
                image = pygame.Surface((128, 128), pygame.SRCALPHA)
                image.fill((255, 0, 0))

            self._loaded_images[picture_name] = image

        return self._loaded_images[picture_name]

    def load_image_sheet(self, sheet_name: str)->None:
        if sheet_name not in self._loaded_images:
            try:
                image = pygame.image.load(json_handler._load_json_file(IMAGE_DATA)["Sheets"][sheet_name]).convert_alpha()
            except (KeyError, FileNotFoundError):
                image = pygame.Surface((128, 128), pygame.SRCALPHA)
                image.fill((255, 0, 0))
            self._loaded_images[sheet_name] = image
        return self._loaded_images[sheet_name]

    def load_background_image(self, level_num: int, room: int) -> pygame.Surface:
        room_key = f"Room {room}"
        room_data = data.load_level_data(level_num,"background")
        image_string = room_data[room_key]
        try:
            background_image = pygame.image.load(image_string).convert_alpha()
        except (KeyError, FileNotFoundError):
            background_image = pygame.Surface((1200, 800), pygame.SRCALPHA)
            background_image.fill((255, 50, 125))
        return background_image

class Image_Animator:
    def __init__(self,name:str,frame:int = 0, change_time:int = 200)-> None:
        self.name = name
        self.frame = frame
        self.change_time = change_time
        self.start_time = pygame.time.get_ticks()
        self.frames:list[pygame.Surface] = []
        self._loaded_frames = {}

    def get_image(self,name:str,frame:int,frame_count:int,width:int,height:int,sheet_size:list)->pygame.Surface:
        sheet = my_image.load_image_sheet(name)
        source_w = sheet_size[0]//frame_count
        source_h = sheet_size[1]
        rect = pygame.Rect(frame * source_w,0,source_w,source_h)
        image = pygame.Surface((source_w,source_h),pygame.SRCALPHA).convert_alpha()
        image.set_colorkey((255,255,255))
        image.blit(sheet,(0,0),rect)
        image = pygame.transform.smoothscale(image,(width,height))

        return image

    def load_frames(self,name:str,frame_count:int,width:int,height:int,sheet_size:list)->None:
        self.frames = [self.get_image(name,i,frame_count,width,height,sheet_size) for i in range(frame_count)]

    def play(self,frame_count:int)->pygame.Surface:
        current_time = pygame.time.get_ticks()
        if (current_time - self.start_time) > self.change_time:
            self.frame = (self.frame + 1) % frame_count
            self.start_time = current_time
        return self.frames[self.frame]

    def get_frames(self, name: str, frame_count: int, w: int, h: int,sheet_size) -> list[pygame.Surface]:
        key = (name, frame_count, w, h)
        if key not in self._loaded_frames:
            animator = Image_Animator(name)
            animator.load_frames(name, frame_count, w, h,sheet_size)
            self._loaded_frames[key] = animator.frames
        return self._loaded_frames[key]

my_image:Image_Handler = Image_Handler()



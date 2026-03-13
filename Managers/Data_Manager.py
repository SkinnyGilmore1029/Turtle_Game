import json
from pathlib import Path
import sys


if getattr(sys, 'frozen', False):  # PyInstaller exe
    PROJECT_ROOT = Path(sys._MEIPASS)  # PyInstaller temp folder
else:
    PROJECT_ROOT = Path(__file__).resolve().parent.parent


JSON_DATA_DIR = PROJECT_ROOT / "Utility"/ "JSON Data"
LEVEL_1_JSON = JSON_DATA_DIR / "Level1"
LEVEL_2_JSON = JSON_DATA_DIR / "Level2"
LEVEL_3_JSON = JSON_DATA_DIR / "Level3"
LEVEL_4_JSON = JSON_DATA_DIR / "Level4"
LEVEL_5_JSON = JSON_DATA_DIR / "Level5"
LEVEL_6_JSON = JSON_DATA_DIR / "Level6"
LEVEL_7_JSON = JSON_DATA_DIR / "Level7"
LEVEL_8_JSON = JSON_DATA_DIR / "Level8"

class Json_Manager:
    def __init__(self):
        self._cached_data = {}

    def _load_json_file(self, path: str) -> dict:
        path_obj = Path(path)  # use pathlib
        if path_obj not in self._cached_data:
            with path_obj.open('r', encoding='utf-8') as file:
                self._cached_data[path_obj] = json.load(file)
        return self._cached_data[path_obj]

json_handler = Json_Manager()

class DataManager:

    def load_level_data(self,level_num:int,datatype:str)->dict[str,dict]:
        path = f"Utility/JSON Data/Level{level_num}/Level{level_num}_{datatype}.json"
        return json_handler._load_json_file(path)

    def from_cutscene_json(self)->dict[dict[str,str|int]]:
        path = f"Utility/JSON Data/Cutscene.json"
        return self._load_json_file(path)


    def get_player_start(self, level_num:int)->list[int,int]:
        player_spot_data = self.load_level_data(level_num,"background")
        player_spot = player_spot_data["Starting Spot"]
        return player_spot

    def get_room2_location(self, level_num:int)->str:
        room_location_data = self.load_level_data(level_num,"background")
        room_location = room_location_data['Room 2 Location']
        return room_location



# Initialize the data manager once:
data = DataManager()
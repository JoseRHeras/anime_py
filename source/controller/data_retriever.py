import json

from source.model.api import API
from typing import Dict, List
from source.model.anime_library import AnimeLibrary



class DataRetriever:

    def __init__(self) -> None:
        self.__load_commands_mapping()
        self.api: API = API()
        self.anime_library: AnimeLibrary = AnimeLibrary()
        self.function_map: Dict = {
            "season+list_view": self.get_season_anime
        }
        self.active_function = None 

    def __load_commands_mapping(self):
        with open("data.json", "r") as file:
            data = json.load(file)
            self.commands_mapping = data['commands_mapping']


    def get_season_anime(self) -> List:
        data = self.anime_library.current_season_animes()
        return data


    def load_parameters(self, parameters: List) -> None:
        key = parameters[0]
        self.active_function = self.function_map[self.commands_mapping[key]]
        
    def get_data(self):
        return self.active_function()


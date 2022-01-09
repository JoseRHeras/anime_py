import json


from typing import Dict, List
from source.model.anime_library import AnimeLibrary



class DataRetriever:

    def __init__(self) -> None:
        self.mapper = APICallsFunctionManager()

    def load_parameters(self, parameters: List) -> None:
        self.mapper.set_active_function_with(parameters=parameters)
        
    def get_data(self):
        return self.mapper.make_call_and_get_data()



class APICallsFunctionManager:
    def __init__(self) -> None:
        self.__load_commands_mapping()
        self.anime_library: AnimeLibrary = AnimeLibrary()
        self.function_map: Dict = {
            "season+list_view": self.get_simplified_list_of_seasonal_animes
        }
        self.active_function = None 

    def __load_commands_mapping(self):
        with open("data.json", "r") as file:
            data = json.load(file)
            self.commands_mapping = data['commands_mapping']

    def get_simplified_list_of_seasonal_animes(self) -> List:
        data = self.anime_library.current_season_animes()
        return data

    def set_active_function_with(self, parameters: List) -> None:
        key = parameters[0]
        self.active_function = self.function_map[self.commands_mapping[key]]

    def make_call_and_get_data(self):
        return self.active_function()


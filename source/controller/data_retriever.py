import json


from typing import Dict, List
from source.model.anime_library import AnimeLibrary



class DataRetriever:

    def __init__(self) -> None:
        self.mapper = APICallsFunctionManager()

    def load_parameters(self, parameters: List) -> None:
        # key = "+".join(parameters)
        # self.mapper.set_active_function_with(key=key)
        self.mapper.load_api_call_parameters(
            api_call_parameters=parameters[0], 
            view_being_loaded=parameters[1]
        )
        
    def get_data(self) -> List:
        return self.mapper.make_call_and_get_data()



class APICallsFunctionManager:
    def __init__(self) -> None:
        self.load_commands_mapping()
        self.anime_library: AnimeLibrary = AnimeLibrary()
        self.function_map: Dict = {
            "list_view": self.get_simplified_list_of_seasonal_animes,
            "detailed_view": self.get_detailed_anime_data,
        }
        self.active_function = None
        self.parameter:str = ""
        self.view_key:str = ""

    def load_commands_mapping(self):
        with open("data.json", "r") as file:
            data = json.load(file)
            self.commands_mapping = data['commands_mapping']

    def get_simplified_list_of_seasonal_animes(self) -> List:
        data = self.anime_library.current_season_animes()
        return data

    def get_detailed_anime_data(self):
        return self.anime_library.detailed_anime(anime_id=self.parameter)

    # Functions exposed to client
    def load_api_call_parameters(self, view_being_loaded:str, api_call_parameters:str) -> None:
        self.parameter = api_call_parameters
        self.view_key = view_being_loaded
        
        self.set_active_function_with(key=view_being_loaded)

    def set_active_function_with(self, key:str) -> None:
        self.active_function = self.function_map[key]

    def make_call_and_get_data(self):
        return self.active_function()


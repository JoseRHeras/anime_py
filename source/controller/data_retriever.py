import json

from source.model.api import API
from typing import Dict, List



class DataRetriever:

    def __init__(self) -> None:
        self.__load_cmd_data()
        self.api: API = API()
        self.function_map: Dict = {
            "season+list_view": self.get_season_anime
        }
        self.operation = None 

    def __load_cmd_data(self):
        with open("data.json", "r") as file:
            data = json.load(file)
            self.cmd_data = data['cmd_data']


    def get_season_anime(self, season:str=None):
        if not season:
            return ['Current Season Animes', "Will be displayed here", "No matter what you think"]
        
        return ['Current Season Animes', "Will be displayed here"]


    def load_commands(self, cmd: List) -> None:
        key = "".join([str(x) for x in cmd])
        function_key = f"{self.cmd_data[key][0]}+{self.cmd_data[key][1]}"
        self.operation = self.function_map[function_key]
        
    def get_data(self):
        return self.operation()

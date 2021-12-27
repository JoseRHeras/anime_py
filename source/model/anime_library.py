from os import times
from typing import Dict, List
from .api import API
from source.utilities import load_saved_data, save_data_in_file

class AnimeLibrary:

    def __init__(self) -> None:
        self.saved_data: Dict = load_saved_data()
        self.api: API = API()

    def current_season_animes(self) -> List:
        if "current_season" in self.saved_data:
            data = self.saved_data["current_season"]
            return extract_title_and_id_from_data(data=data)

        data = self.api.get_current_season_animes()
        save_data_in_file(key="current_season", data=data)

        return extract_title_and_id_from_data(data=data)

def extract_title_and_id_from_data(data) -> List:    
    return [[anime["attributes"]["slug"], anime["id"]] for anime in data]  
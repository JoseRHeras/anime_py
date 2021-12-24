from typing import Dict
from .api import API
from source.utilities import load_saved_data, save_data_in_file

class AnimeLibrary:

    def __init__(self) -> None:
        self.saved_data: Dict = load_saved_data()
        self.api: API = API()

    def current_season_animes(self):
        if "current_animes" in self.saved_data:
            return self.saved_data["current_season"]
        
        data = self.api.get_current_season_animes()
        save_data_in_file(key="current_animes", data=data)

        return data


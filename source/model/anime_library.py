from dataclasses import asdict
from typing import Dict, List

from source.model.data_models import Show
from .api import API
from source.utilities import load_saved_data, save_data_in_file

class AnimeLibrary:

    def __init__(self) -> None:
        self.saved_data: Dict = load_saved_data()
        self.api: API = API()

    def current_season_animes(self) -> List:
        if "current_season" in self.saved_data:
            data = self.saved_data["current_season"]
            data = [Show(**x) for x in data]
            return extract_title_and_id_from_data(data=data)

        data = self.api.get_current_season_animes()
        save_data_in_file(key="current_season", data=[asdict(x) for x in data])

        return extract_title_and_id_from_data(data=data)

    def detailed_anime(self, anime_id:str) -> List:
        data = self.api.get_detailed_anime_data(id=anime_id)
        data = data.list_representation()
        return data

    def animes_by_search_term(self,term:str) -> List:
        data = self.api.get_animes_by_searchtearm(term=term)
        return extract_title_and_id_from_data(data=data)


def extract_title_and_id_from_data(data: List[Show]) -> List:
    return [[x.title_id, x.canonical_title] for x in data]  
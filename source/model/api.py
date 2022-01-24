import requests
from typing import Any, Dict, List
from source.model.data_models import Show, parse_to_show_object
from source.endpoints import CURRENT_ANIMES, DETAILED_ANIME, SEARCH_BY_TERM


class API:

    # def get_current_season_animes(self) -> List:
    #     endpoint = "https://kitsu.io/api/edge/anime?filter[status]=current"
    #     animes: List = []
    #     while True:
    #         data: Any = requests.get(endpoint)
    #         data = data.json()
    #         animes = animes + data['data']

    #         if("next" not in data['links']): break

    #         endpoint = data['links']['next']
               
    #     return parse_data_to_list(animes)

    def get_current_season_animes(self) -> List[Show]:
        endpoint = "https://kitsu.io/api/edge/anime?filter[status]=current"
        animes: List = []
        count = 0
        while True:
            data: Any = requests.get(endpoint)
            data = data.json()
            animes = animes + data['data']

            if count == 3: break

            endpoint = data['links']['next']
            count += 1
               
        return parse_data_to_list(animes)

    def get_detailed_anime_data(self, id:str) -> Show:
        endpoint = f"{DETAILED_ANIME}{id}"
        try:
            data = requests.get(url=endpoint)
            data = data.json()["data"]
            return parse_to_show_object(data=data)
        except:
            return Show()

    def get_animes_by_searchtearm(self, term:str) -> List[Show]:
        endpoint = f"{SEARCH_BY_TERM}/{term}"
        query_results = requests.get(url=endpoint)
        data: Dict = query_results.json()
        
        return parse_data_to_list(data=data['data'])
            

def parse_data_to_list(data: List) -> List[Show]:
    return [parse_to_show_object(x) for x in data]


   

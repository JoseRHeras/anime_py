import requests
from typing import Any, List
from source.model.data_models import Show, parse_to_show_object



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

    def fetch_data_from(self, link):
        pass



def parse_data_to_list(data: List) -> List[Show]:
    return [parse_to_show_object(x) for x in data]
    
   

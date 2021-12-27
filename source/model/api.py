import requests
from typing import Any, List


class API:

    def get_current_season_animes(self) -> List:
        endpoint = "https://kitsu.io/api/edge/anime?filter[status]=current"
        animes: List = []
        while True:
            data: Any = requests.get(endpoint)
            data = data.json()
            animes = animes + data['data']

            if("next" not in data['links']): break

            endpoint = data['links']['next']
            
        return animes

    def fetch_data_from(self, link):
        pass



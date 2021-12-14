import json
import requests
from source.endpoints import CURRENT_ANIMES

class API:

   
    def get_current_season_animes(self):
        data = requests.get(CURRENT_ANIMES)
        return data.json()

    
    def fetch_data_from(self, link):
        return requests.get(link)

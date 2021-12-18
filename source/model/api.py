import json
from source.endpoints import CURRENT_ANIMES

dummy_data = {
    "current_animes" : [
        ["Title number 1", "ID"],
        ["Title number 1", "ID"],
        ["Title number 1", "ID"],
        ["Title number 1", "ID"],
        ["Title number 1", "ID"],
        ["Title number 1", "ID"],
        ["Title number 1", "ID"],
        ["Title number 1", "ID"],
        ["Title number 1", "ID"],
        ["Title number 1", "ID"],
        ["Title number 1", "ID"]
    ]
}

class API:

   
    def get_current_season_animes(self):
        # data = requests.get(CURRENT_ANIMES)
        # return data.json()
        return dummy_data['current_animes']

    
    def fetch_data_from(self, link):
        # return requests.get(link)
        pass

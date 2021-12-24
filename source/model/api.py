import requests
# from source.endpoints import CURRENT_ANIMES

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
        endpoint = "https://kitsu.io/api/edge/anime?filter[status]=current"
        animes = []
        while True:
            data = requests.get(endpoint)
            data = data.json()
            animes = animes + data['data']

            if("next" not in data['links']): break

            endpoint = data['links']['next']
            
        return data

    def fetch_data_from(self, link):
        pass



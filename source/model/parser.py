from .api import API


class Parser:

    # def initilize_season_animes(self):
    #     self.airing_anime_collection = AiringAnimeCollection(API.get_this_season_animes())

    def current_season_animes(self):
        return self.airing_anime_collection.titles()




class AiringAnimeCollection:
    
    def __init__(self, data):
        self.animes = data['data']
        self.meta = data['meta']
        self.links = data['links']

    def titles(self):
        titles = []
        for anime in self.animes:
            titles.append(self._get_title(anime))
        
        return titles

    def _get_title(self, anime):
        return anime['attributes']['titles']['en']





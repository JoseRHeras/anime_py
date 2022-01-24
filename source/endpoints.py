# The following program makes use of the KitsuAPI for all endpoint requests
import json
from source.utilities import retrive_current_season

# Load base url
with open('data.json', 'r') as file:
    data = json.load(file)
    KITSU_BASE_URL = data['endpoint']['kitsu_api_base_url']

# Current Season Endpoint
year, season = retrive_current_season()
CURRENT_ANIMES = f"{KITSU_BASE_URL}/anime?filter%5Bseason%5D={season}&filter%5BseasonYear%5D={year}"

# Detailed version of an anime
DETAILED_ANIME = F"{KITSU_BASE_URL}/anime/"

# Search by term endpoint
SEARCH_BY_TERM = f"{KITSU_BASE_URL}/anime?filter[text]="
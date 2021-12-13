# The following program makes use of the KitsuAPI for all endpoint requests
import json
from config.utilities import retrive_current_season

# Load base url
with open('data.json', 'r') as file:
    data = json.load(file)
    BASE_URL = data['endpoint']['base_url']

# Current Season Endpoint
year, season = retrive_current_season()
CURRENT_ANIMES = f"{BASE_URL}/anime?filter%5Bseason%5D={season}&filter%5BseasonYear%5D={year}"
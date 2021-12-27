import json
import datetime

from os import system
from typing import Dict, List

# Utilites function which return current year and season
def retrive_current_season():
    from datetime import date
    
    with open("data.json", "r") as file:
        data = json.load(file)
        seasons = data['seasons']

    current_date = date.today()
    month = current_date.month
    
    for key in seasons:
        if month in seasons[key]:
            month = key
            break

    return(current_date.year, month)

# Function used to clear cmd 
def clear_cmd_screen() -> None:
    system("cls")


def build_string_from_list(data: List) -> str:
    return "".join([str(line) + "\n" for line in data])


def build_string_from_dict(data: Dict) -> str:
    str_representation = ''
    
    for key in data:
        str_representation += f"{key}: {data[key][0]} \n"

    return str_representation


# Loads saved data from json file
def load_saved_data():
    with open("api_saves.json") as f:
        data = json.load(f)
    
    return data

# Saves data into json file
def save_data_in_file(key, data):
    with open("api_saves.json") as f:
        old_save = json.load(f)
        
    with open("api_saves.json", "w") as f:
        new_save = {**old_save, key:data }
        json.dump(new_save, f, indent=2)

    
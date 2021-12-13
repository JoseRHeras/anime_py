import json

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

def clear_cmd_screen() -> None:
    system("cls")


def build_string_from_list(data: List) -> str:
    return "".join([str(line) + "\n" for line in data])


def build_string_from_dict(data: Dict) -> str:
    str_representation = ''
    
    for key in data:
        str_representation += f"{key}: {data[key][0]} \n"

    return str_representation

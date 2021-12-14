from abc import ABC
import json
from source.view.view import View
from typing import Dict, List
from source.utilities import build_string_from_list, build_string_from_dict

with open("data.json", 'r') as f:
    data = json.load(f)
    data = data['messages']





class MainMenuView(View):
    
    def __init__(self) -> None:
        self.id: str = "main"
        self.options: Dict = data['main_menu']
        self.content: List[str] = ["Welcome to Main Screen"]

    def update_view(self, content: List) -> None:
        self.content = content

    def make_screen(self) -> str:
        data = build_string_from_list(self.content)
        options = build_string_from_dict(self.options)
        return f"{data}\n{options}"

    def screen_options(self) -> Dict:
        return self.options


class SearchView(View):
    def __init__(self) -> None:
        self.id: str = "search"
        self.options: Dict = data['search_view']
        self.content: List[str] = ['Search Screen']

    def update_view(self, content: List) -> None:
        self.content = content

    def make_screen(self) -> str:
        data = build_string_from_list(self.content)
        options = build_string_from_dict(self.options)
        return f"{data}\n{options}"

    def screen_options(self) -> Dict:
        return self.options


class ListView(View):
    def __init__(self) -> None:
        self.id: str = "list_view"
        self.options: Dict = data["list_view"]
        self.content: List = ["List of Animes"]

    def update_view(self, content: List) -> None:
        self.content = content

    def make_screen(self) -> str:
        data = build_string_from_list(self.content)
        options = build_string_from_dict(self.options)
        return f"{data}\n{options}"

    def screen_options(self) -> Dict:
        return self.options




def construct_view(type: str) -> View:
    
    views = {
        "main" : MainMenuView(),
        "search_view" : SearchView(),
        "list_view" : ListView()
    }
    return views[type]



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

    def available_options(self) -> Dict:
        return self.options

    def transform_into_string(self) -> str:
        return ""

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

    def available_options(self) -> Dict:
        return self.options

    def transform_into_string(self) -> str:
        return ""


class ListView(View):
    def __init__(self) -> None:
        self.id: str = "list_view"
        self.options: Dict = data["list_view"]
        self.content: List = []

    def content_to_string(self) -> str:
        content = ""
        for index, item in enumerate(self.content):
            
            content += f"{index + 1}: {item[0]}\n"
            
        return content
        

    def update_view(self, content: List) -> None:
        self.content = content

    def make_screen(self) -> str:
        options_str = build_string_from_dict(self.options)
        content_str = self.content_to_string()
        return f"{content_str}\n{options_str}"
    
    

    def available_options(self) -> Dict:
        return self.options

    




def construct_view(type: str) -> View:
    
    views = {
        "main" : MainMenuView(),
        "search_view" : SearchView(),
        "list_view" : ListView()
    }
    return views[type]



from abc import ABC
import json
from source.model.data_models import Show
from source.view.view import View
from typing import Dict, List, Tuple
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


    def get_user_input(self) -> List[str]:
        
        while True:
            usr_input = input("Select an option: ")
            if str(usr_input) in self.options: break
            
            print(f"Not a valid option")

        return self.options[str(usr_input)][1]

    def available_options(self) -> Dict:
        return self.options


class ListView(View):
    def __init__(self) -> None:
        self.id: str = "list_view"
        self.maps_to: str = "detailed_view"
        self.options: Dict = data["list_view"]
        self.content: List = []

    def __content_to_string(self) -> str:
        content = ""
        for index, item in enumerate(self.content):
            content += f"{index + 1}: {item[1]}\n"
            
        return content
        
    def update_view(self, content: List) -> None:
        self.content = content

    def make_screen(self) -> str:
        options_str = build_string_from_dict(self.options)
        content_str = self.__content_to_string()
        return f"{content_str}\n{options_str}"
    
    def _evaluate_content_with_id(self, id: str) -> bool:
        return False

    def get_user_input(self) -> List[str]:
        
        while(True): 
            usr_input = input("Select an option: ")

            is_id_present = self._evaluate_content_with_id(id=usr_input)

            if is_id_present or usr_input == "exit": break
            
            print(f"Parameters entered does not match an item. Try again!!")

        return self.options[str(usr_input)][1]
    
    def available_options(self) -> Dict:
        return self.options

    
# Factory for view
def construct_view(type: str) -> View:
    
    views = {
        "main" : MainMenuView(),
        "list_view" : ListView()
    }
    return views[type]


def get_valid_user_input(valid_input: Dict) -> List[str]:
    
    user_input = ""

    while(True):
        user_input = input("Select an option: ")
        
        if str(user_input) in valid_input:
            return valid_input[str(user_input)]
        
        print(f"The option {user_input} is not a valid option!!!")
import json
from source.view.view import View
from typing import Dict, List
from source.utilities import build_string_from_dict


class MainMenuView(View):
    
    def __init__(self) -> None:
        self._initialize_options()
        self.content: List[str] = ["Welcome to Main Screen"]

    def _initialize_options(self) -> None:
        with open("data.json", 'r') as f:
            data = json.load(f)  

        self.options: Dict = data['main_menu']

    def _content_to_string(self) -> str:
        return "".join([f"{line}\n" for line in self.content])

    def _options_to_string(self) -> str:
        return "\n".join([f"{key} -> {self.options[key][0]}" for key in self.options.keys()])
        
    def update_view(self, content: List) -> None:
        pass

    def make_screen(self) -> str:
        return f"{self._content_to_string()}\n{self._options_to_string()}\n"


    def get_user_input(self) -> List[str]:
        
        while True:
            usr_input = input("Select an option: ")
            if usr_input in self.options: return self.options[usr_input][1]
            
            print("Not a valid option\n")

        


class ListView(View):
    def __init__(self) -> None:
        self.content_from_api: List = []
        self.view_content: List = [
            "-> Enter the ID of the anime you wish to see more detailed data",
            "-> Enter exit to go back to previous"
        ]

    def _content_to_string(self) -> str:
        content = ""
        for index, item in enumerate(self.content_from_api):
            content += f"{index + 1}: {item[1]}\n"
            
        return content
    
    def _view_content_to_string(self) -> str:
        return "\n".join(self.view_content)

    def update_view(self, content: List) -> None:
        self.content_from_api = content

    def is_input_valid(self, id: str) -> bool:           #Evaluates if input is a number and within a range
        if not str.isnumeric(id): return False
        if int(id) - 1 > len(self.content_from_api) - 1 or int(id) < 1: return False

        return True

    def make_screen(self) -> str:
        return f"{self._content_to_string()}\n{self._view_content_to_string()}\n"
    
    def get_id_from_content(self, id: int) -> str:

        for index, item in enumerate(self.content_from_api):
            if index == int(id): 
                key = item[0]
                break
        return key

    def get_user_input(self) -> List[str]:
        
        while(True): 
            usr_input = input("Select an option: ")

            if usr_input == "exit": return ["_", "exit"]
                
            if self.is_input_valid(id=usr_input):
                return [ self.get_id_from_content(id=int(usr_input) - 1), "detailed_view"] 
                
            print(f"Parameters entered does not match an item. Try again!!")

    
class DetailedView(View):

    def __init__(self) -> None:
        self.content_from_api: List = []
        self.view_content: List = ["Enter exit to go back to previous"]

    def _content_to_string(self) -> str:
        return "".join([f"{line}\n" for line in self.content_from_api])
    
    def _view_content_to_str(self) -> str:
        return "\n".join(self.view_content)

    def update_view(self, content: List) -> None:
        self.content_from_api = content

    def make_screen(self) -> str:
        return f"{self._content_to_string()}\n{self._view_content_to_str()}\n"

    def get_user_input(self) -> List[str]:
        while True:
            usr_input:str = input("Select an option: ")
            if usr_input == "exit": return ["_", "exit"]
        
          
class SearchView(View):

    def __init__(self) -> None:
        self.view_content: List = ["Search Box: ", "Type the anime you want to search or \'Enter exit to go back to previous \'",]

    def _content_to_string(self):
        return "".join([f"{line}\n" for line in self.view_content])
    
    def update_view(self, content: List) -> None:
        pass

    def make_screen(self) -> str:
        return self._content_to_string()

    def get_user_input(self) -> List[str]:
        valid_length = 2
        while True:
            usr_input = input("Anime Name: ")

            if usr_input == "exit": return ["_", "exit"]
            
            if len(usr_input) > valid_length: return [str(usr_input), "search_query_list_view"]

            if len(usr_input) < valid_length and len(usr_input) > 0:
                print(f"Search word must be at least {valid_length + 1} characters long")
            else:
                print("Invalid input! Please try again")


# View factory function
def construct_view(type: str) -> View:
    
    views = {
        "main" : MainMenuView(),
        "list_view" : ListView(),
        "detailed_view": DetailedView(),
        "search_view": SearchView(),
        "search_query_list_view": ListView()
    }
    return views[type]

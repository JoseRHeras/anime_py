import json
from source.view.view import View
from typing import Dict, List
from source.utilities import build_string_from_dict

with open("data.json", 'r') as f:
    data = json.load(f)
    data = data['messages']


class MainMenuView(View):
    
    def __init__(self) -> None:
        self.options: Dict = data['main_menu']
        self.content: List[str] = ["Welcome to Main Screen"]

    def _content_to_string(self) -> str:
        return "".join([f"{line}\n" for line in self.content])
        
    def update_view(self, content: List) -> None:
        self.content = content

    def make_screen(self) -> str:
        content = self._content_to_string()
        options = build_string_from_dict(self.options)
        return f"{content}\n{options}"


    def get_user_input(self) -> List[str]:
        
        while True:
            usr_input = input("Select an option: ")
            if str(usr_input) in self.options: break
            
            print(f"Not a valid option")

        return self.options[str(usr_input)][1]


class ListView(View):
    def __init__(self) -> None:
        self.options: Dict = data["list_view"]
        self.content: List = []

    def _content_to_string(self) -> str:
        content = ""
        for index, item in enumerate(self.content):
            content += f"{index + 1}: {item[1]}\n"
            
        return content
        
    def update_view(self, content: List) -> None:
        self.content = content

    def make_screen(self) -> str:
        options_str = build_string_from_dict(self.options)
        content_str = self._content_to_string()
        return f"{content_str}\n{options_str}"
    
    def is_input_valid(self, id: str) -> bool:           #Evaluates if input is a number and within a range
        if not str.isnumeric(id): return False
        if int(id) - 1 > len(self.content) - 1 or int(id) < 1: return False

        return True

    def get_id_from_content(self, id: int) -> str:

        for index, item in enumerate(self.content):
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
        self.content: List = []
        self.options: Dict = data["detailed_view"]

    def _content_to_string(self) -> str:
        return "".join([f"{line}\n" for line in self.content])

    def update_view(self, content: List) -> None:
        self.content = content

    def make_screen(self) -> str:
        page_body = self._content_to_string()
        page_options = build_string_from_dict(self.options)

        return f"{page_body}\n{page_options}"

    def get_user_input(self) -> List[str]:
        while True:
            usr_input:str = input("Select an option: ")
            if usr_input == "exit": break
        
        return self.options[usr_input][1]


    
class SearchView(View):

    def __init__(self) -> None:
        self.view_conten: List = ["Search Box: ", "Type the anime you want to search or \'Enter exit to go back to previous \'",]

    def _content_to_string(self):
        return "".join([f"{line}\n" for line in self.view_conten])
    
    def update_view(self, content: List) -> None:
        pass

    def make_screen(self) -> str:
        return self._content_to_string()

    def get_user_input(self) -> List[str]:
        
        while True:
            usr_input = input("Anime Name: ")

            if usr_input == "exit": return ["_", "exit"]
            
            if len(usr_input) > 0: return [str(usr_input), "search_query_list_view"]

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

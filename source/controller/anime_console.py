from source.view.view import View
from typing import List
from source.utilities import clear_cmd_screen
from source.view.views import construct_view
from source.controller.data_retriever import DataRetriever


class AnimeConsole:

    def __init__(self) -> None:
        self.view_memory = ViewMemory()
        self.data_retriever: DataRetriever = DataRetriever()

        self._initialize_first_view()
    
    def _initialize_first_view(self) -> None:       
        self.view: View = construct_view("main")
        self.data: List = []
        self.terminate_loop: bool = False
        
    def _create_and_load_view(self, view_key:str) -> None:
        self.view = construct_view(view_key)

    def _get_view_parameters(self):
        data = self.view.available_options()
        

    def _retrieve_data_and_update_view(self, user_input:str, view_key:str) -> None:
        view_parameters = self._get_view_parameters()
        self.data_retriever.load_parameters([f"{user_input}{view_key}"])
        data = self.data_retriever.get_data()
        self.view.update_view(data)
    
    def _save_current_view_in_stack(self) -> None:
       self.view_memory.append(self.view)

    
    def _generate_view_key(self, user_input:str) -> str:
        return self.view.available_options()[user_input][1]

    def _update_state_with_user_input(self, user_input:str) -> None:
        new_view = user_input[1]

        self._save_current_view_in_stack()

        self._create_and_load_view(view_key=new_view)
        # self._retrieve_data_and_update_view(user_input=user_input, view_key=view_key)

    def _display_screen_in_cmd(self) -> None:
        screen = self.view.make_screen()
        print(screen)

    def render_screen(self) -> None:
        clear_cmd_screen()
        self._display_screen_in_cmd()

    def wait_for_user_input(self) -> None:

        user_input = self.view.get_user_input()

        if user_input[1] == "exit":
            
            if self.view_memory.is_empty():
                # Terminate the program
                self.terminate_loop = True
                return
            #Load saved view
            self.view, self.data =self.view_memory.retrieve()
               
        else:
            self._update_state_with_user_input(user_input=user_input)

class Console:
    
    def __init__(self) -> None:
        self.view_memory = ViewMemory()
        self.data_retriever: DataRetriever = DataRetriever()

        self.initialize_main_view()
    
    def initialize_main_view(self) -> None:       
        self.view: View = construct_view("main")
        self.data: List = []
        self.terminate_loop: bool = False

    def render_view_to_screen(self) -> None:
        clear_cmd_screen()
        print(self.view.make_screen())                              # Print the view contents to the screen

    def save_current_state(self) -> None:
        self.view_memory.append(view=self.view, data=self.data)

    def create_and_load_new_state(self, view:str) -> None:
        self.view = construct_view(view)
        self.data = []

    def get_data_and_update_view(self, parameters: List) -> None:
        self.data_retriever.load_parameters(parameters=parameters)
        data: List = self.data_retriever.get_data()
        self.view.update_view(data)

    def update_state_with_next_view(self, data: List) -> None:
        self.save_current_state()
        self.create_and_load_new_state(data[1])
        self.get_data_and_update_view(parameters=data)

    def get_usr_input_and_update_state(self) -> None:
        usr_input = self.view.get_user_input()
        
        if usr_input[1] == "exit":
            if self.view_memory.is_empty():
                self.terminate_loop = True                          # Terminate the program
                return
            
            self.view, self.data = self.view_memory.retrieve()      #Load saved view     
        else:
            self.update_state_with_next_view(usr_input)
        


class ViewMemory:

    def __init__(self) -> None:
        self.memoryStack: List = []

    def append(self, view: View, data: List = []) -> None:
        data = [view, data]
        self.memoryStack.append(data)

    def retrieve(self) -> List:
        return self.memoryStack.pop()
    
    def is_empty(self) -> bool:
        if len(self.memoryStack) > 0: return False

        return True
        


def get_valid_user_input(valid_input) -> str:
    
    user_input = ""

    while(True):
        user_input = input("Select an option: ")
        
        if str(user_input) in valid_input:
            return str(user_input)
        
        print(f"The option {user_input} is not a valid option!!!")
    
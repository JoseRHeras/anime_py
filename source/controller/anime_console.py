from source.view.view import View
from typing import Dict, List
from source.utilities import clear_cmd_screen
from source.view.views import construct_view
from source.controller.data_retriever import DataRetriever


class AnimeConsole:

    def __init__(self) -> None:
        self.__initialize()
    
    def __initialize(self) -> None:
        self.view_stack: List[View] = []
        self.view: View = construct_view("main")
        self.terminate_loop: bool = False
        self.data_retriever: DataRetriever = DataRetriever()

    def __create_and_load_view(self, view_key:str) -> None:
        self.view = construct_view(view_key)

    def __get_view_parameters(self):
        data = self.view.available_options()
        

    def __retrieve_data_and_update_view(self, user_input:str, view_key:str) -> None:
        view_parameters = self.__get_view_parameters()
        self.data_retriever.load_parameters([f"{user_input}{view_key}"])
        data = self.data_retriever.get_data()
        self.view.update_view(data)
    
    def __save_current_view_in_stack(self) -> None:
        self.view_stack.append(self.view)

    
    def __generate_view_key(self, user_input:str) -> str:
        return self.view.available_options()[user_input][1]

    def __update_state_with_user_input(self, user_input:str) -> None:
        self.__save_current_view_in_stack()
        view_key = self.__generate_view_key(user_input=user_input)
        self.__create_and_load_view(view_key=view_key)
        self.__retrieve_data_and_update_view(user_input=user_input, view_key=view_key)

    def __display_screen_in_cmd(self) -> None:
        screen = self.view.make_screen()
        print(screen)

    def render_screen(self) -> None:
        clear_cmd_screen()
        self.__display_screen_in_cmd()

    def wait_for_user_input(self) -> None:
        user_input = get_valid_user_input(self.view.available_options())

        if user_input == "exit":
            
            if len(self.view_stack) < 1:
                # Terminate the program
                self.terminate_loop = True
                return
            #Load saved view
            self.view = self.view_stack.pop()
               
        else:
            self.__update_state_with_user_input(user_input=user_input)
            
            
def get_valid_user_input(valid_input) -> str:
    
    user_input = ""

    while(True):
        user_input = input("Select an option: ")
        
        if str(user_input) in valid_input:
            return str(user_input)
        
        print(f"The option {user_input} is not a valid option!!!")
    
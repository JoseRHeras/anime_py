from source.view.view import View
from typing import Dict, List
from source.utilities import clear_cmd_screen
from source.view.views import construct_view
from source.controller.data_retriever import DataRetriever

NUMBER_OF_TRIES = 5

class AnimeConsole:

    def __init__(self) -> None:
        self.__initialize()
    
    def __initialize(self):
        self.view_stack: List[View] = []
        self.view: View = construct_view("main")
        self.terminate_loop: bool = False
        self.data_retriever: DataRetriever = DataRetriever()
        
    def render_screen(self) -> None:
        clear_cmd_screen()
        screen = self.view.make_screen()
        print(screen)
    


    def wait_for_user_input(self) -> None:
        user_input = get_valid_user_input(self.view.screen_options())


        if user_input == "exit":
            
            if len(self.view_stack) < 1:
                # Terminate the program
                self.terminate_loop = True
                return
            #Load saved view
            self.view = self.view_stack.pop()
               
        else:

            self.view_stack.append(self.view)
            key: str = self.view.screen_options()[user_input][1]
            screen = construct_view(key)

            self.view = screen
            #Get screen mapped to choice
            #Run queries related to choice
            #Update screen with data
            #Let main loop take care of rendering the screen
            
 
def get_valid_user_input(valid_input) -> str:
    
    user_input = ""

    while(True):
        user_input = input("Select an option: ")
        
        if str(user_input) in valid_input:
            return str(user_input)
        
        print(f"The option {user_input} is not a valid option!!!")
    
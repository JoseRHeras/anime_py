from abc import ABC, abstractmethod
from typing import Dict, List, Tuple

class View(ABC):

    @abstractmethod
    def update_view(self, content: List) -> None:
        """ Takes user input and updates screen content """
        pass

    @abstractmethod
    def make_screen(self) -> str:
        """ Generates screen to be displayed"""
        pass

    @abstractmethod
    def available_options(self) -> Dict:
        """ Returns valid inputs for the following view """
        pass

    @abstractmethod
    def get_user_input(self) -> List[str]:
        """ Returns a list representation of user input"""
        pass

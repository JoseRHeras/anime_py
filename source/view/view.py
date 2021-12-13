from abc import ABC, abstractmethod
from typing import Dict, List

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
    def screen_options(self) -> Dict:
        """ Returns valid inputs for the following view """
        pass
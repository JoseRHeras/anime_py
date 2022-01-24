from dataclasses import dataclass, field
from email.mime import image
from typing import Dict, List

@dataclass
class Show:
    title_id: str = "1"
    links: str = ""
    synopsis: str = ""
    titles: Dict = field(default_factory=dict)
    canonical_title: str = ""
    image: str = ""

    def _get_en_title(self) -> str:
        list_repr = list(self.titles.values())
        return list_repr[0]

    def __str__(self) -> str:
        return f"{self._get_en_title()}\n\n{self.synopsis}\n\nImage Link{self.image}"

    
    def list_representation(self) -> List[str]:
        return [
            f"Title: {self._get_en_title()}\n", 
            f"Synopsis: {self.synopsis}\n", 
            f"Image Link: {self.image}"]


def parse_to_show_object(data:Dict) -> Show:
    return Show(
        title_id=data["id"], 
        links=data["links"]["self"], 
        synopsis=data["attributes"]["synopsis"], 
        titles=data["attributes"]["titles"], 
        canonical_title=data["attributes"]["canonicalTitle"],
        image=data["attributes"]["posterImage"]["original"]
    )
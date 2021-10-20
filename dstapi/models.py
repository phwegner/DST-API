from dataclasses import dataclass
from .apimanager import ApiManager
import requests
from typing import Optional

@dataclass
class Variable:
    name: str
    description: str
    topic: str
    unit: str = "None"
    umbrella: Optional[str] = None
    topic_description: Optional[str] = None 
    umbrella_description: Optional[str] = None
    tooltip: Optional[str] = None

    def __post_init__(self):
        self.umbrella = self.topic if self.umbrella is None else self.umbrella
        self.umbrella_description = self.description if self.umbrella_description is None else self.umbrella_description
        self.tooltip = self.name if self.tooltip is None else self.tooltip 
        self.topic_description = self.topic if self.topic_description is None else self.topic_description

    def save(self, manager: ApiManager):
        body = {
            "topic": self.topic,
            "topic_description": self.topic_description,
            "unit": self.unit,
            "umbrella": self.umbrella,
            "umbrella_description": self.umbrella_description,
            "attribute": self.name,
            "attribute_description": self.description,
            "attribute_tooltip": self.tooltip
        }
        print(f"posting {self.name}")
        response = requests.post(manager.url  + "post/attribute", data = body)
        print(f"Request status code : {response.status_code}")
        print(f"Response : {response.text}")



@dataclass
class Source:
    abbreviation : str
    name : str

    def save(self, manager : ApiManager):
        body = {
            "abbreviation": self.abbreviation, 
            "source": self.name
        }
        print(f"posting {self.name}")
        response = requests.post(manager.url + "post/source", data = body)
        print(f"Request status code : {response.status_code}")
        print(f"Response : {response.text}")


class VariableMapping:
    pass
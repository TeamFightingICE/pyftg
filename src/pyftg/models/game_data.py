from dataclasses import dataclass
from typing import List

from google.protobuf.message import Message

from pyftg.models.base_model import BaseModel


@dataclass
class GameData(BaseModel):
    max_hps: List[int]
    max_energies: List[int]
    character_names: List[str]
    ai_names: List[str]
    
    def get_character_name(self, player: bool):
        return self.character_names[0 if player else 1]
    
    def get_ai_name(self, player: bool):
        return self.ai_names[0 if player else 1]

    def to_dict(self):
        return {
            "max_hps": self.max_hps,
            "max_energies": self.max_energies,
            "character_names": self.character_names,
            "ai_names": self.ai_names
        }

    @classmethod
    def from_dict(cls, data_obj: dict):
        return GameData(
            max_hps=data_obj["max_hps"],
            max_energies=data_obj["max_energies"],
            character_names=data_obj["character_names"],
            ai_names=data_obj["ai_names"]
        )
    
    @classmethod
    def from_proto(cls, proto_obj: Message):
        return GameData(
            max_hps=list(proto_obj.max_hps),
            max_energies=list(proto_obj.max_energies),
            character_names=list(proto_obj.character_names),
            ai_names=list(proto_obj.ai_names)
        )
    
    @classmethod
    def get_default_instance(cls):
        return GameData(max_hps=[0, 0], max_energies=[0, 0], character_names=["", ""], ai_names=["", ""])

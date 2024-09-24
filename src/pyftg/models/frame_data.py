from dataclasses import dataclass, field
from typing import List, Optional

from google.protobuf.message import Message

from pyftg.models.attack_data import AttackData
from pyftg.models.base_model import BaseModel
from pyftg.models.character_data import CharacterData


@dataclass
class FrameData(BaseModel):
    """
    FrameData (BaseModel): Frame data class.
    """

    character_data: List[Optional[CharacterData]] = field(default_factory=lambda: [None, None])
    """
    character_data (List[Optional[CharacterData]]): The character's data of both characters.
    Index 0 is player 1, and index 1 is player 2.
    """
    current_frame_number: int = -1
    """
    current_frame_number (int): The current frame of the round.
    """
    current_round: int = -1
    """
    current_round (int): The current round number.
    """
    projectile_data: List[AttackData] = field(default_factory=list)
    """
    projectile_data (List[AttackData]): The projectile data of both characters.
    """
    empty_flag: bool = True
    """
    empty_flag (bool): If this value is true, no data are available or they are dummy data.
    """
    front: List[bool] = field(default_factory=lambda: [False, False])
    """
    front (List[bool]): The direction the character is facing for two players.\n
    Index 0 is player 1, and index 1 is player 2.\n
    True if the player is facing right, otherwise False.
    """

    def is_front(self, player: bool) -> bool:
        if len(self.front) < 2:
            return False
        return self.front[0 if player else 1]
    
    def get_character(self, player: bool) -> Optional[CharacterData]:
        if len(self.character_data) < 2:
            return None
        return self.character_data[0 if player else 1]
    
    def get_projectiles_by_player(self, player: bool) -> List[AttackData]:
        return [x for x in self.projectile_data if x.player_number == player]
    
    def to_dict(self) -> dict:
        return {
            "character_data": [None if not data else data.to_dict() for data in self.character_data],
            "current_frame_number": self.current_frame_number,
            "current_round": self.current_round,
            "projectile_data": [data.to_dict() for data in self.projectile_data],
            "empty_flag": self.empty_flag,
            "front": self.front
        }

    @classmethod
    def from_dict(cls, data_obj: dict):
        return FrameData(
            character_data=[None if not data else CharacterData.from_dict(data) for data in data_obj["character_data"]],
            current_frame_number=data_obj["current_frame_number"],
            current_round=data_obj["current_round"],
            projectile_data=[AttackData.from_dict(data) for data in data_obj["projectile_data"]],
            empty_flag=data_obj["empty_flag"],
            front=data_obj["front"]
        )
    
    @classmethod
    def from_proto(cls, proto_obj: Message):
        character_data = [None, None]
        if len(proto_obj.character_data) > 0:
            character_data = [CharacterData.from_proto(data) for data in proto_obj.character_data]

        return FrameData(
            character_data=character_data,
            current_frame_number=proto_obj.current_frame_number,
            current_round=proto_obj.current_round,
            projectile_data=list(map(AttackData.from_proto, proto_obj.projectile_data)),
            empty_flag=proto_obj.empty_flag,
            front=list(proto_obj.front)
        )

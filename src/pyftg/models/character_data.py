from dataclasses import dataclass, field
from typing import List

from google.protobuf.message import Message

from pyftg.models.attack_data import AttackData
from pyftg.models.base_model import BaseModel
from pyftg.models.enums.action import Action
from pyftg.models.enums.state import State


@dataclass
class CharacterData(BaseModel):
    player_number: bool = False
    hp: int = 0
    energy: int = 0
    x: int = 0
    y: int = 0
    left: int = 0
    right: int = 0
    top: int = 0
    bottom: int = 0
    speed_x: int = 0
    speed_y: int = 0
    state: State = State.STAND
    action: Action = Action.NEUTRAL
    front: bool = False
    control: bool = False
    attack_data: AttackData = AttackData()
    remaining_frame: int = 0
    hit_confirm: bool = False
    graphic_size_x: int = 0
    graphic_size_y: int = 0
    graphic_adjust_x: int = 0
    hit_count: int = 0
    last_hit_frame: int = 0
    projectile_attack: List[AttackData] = field(default_factory=lambda: [AttackData()] * 3)
    
    def to_dict(self):
        return {
            "player_number": self.player_number,
            "hp": self.hp,
            "energy": self.energy,
            "x": self.x,
            "y": self.y,
            "left": self.left,
            "right": self.right,
            "top": self.top,
            "bottom": self.bottom,
            "speed_x": self.speed_x,
            "speed_y": self.speed_y,
            "state": self.state.to_int(),
            "action": self.action.to_int(),
            "front": self.front,
            "control": self.control,
            "attack_data": self.attack_data.to_dict(),
            "remaining_frame": self.remaining_frame,
            "hit_confirm": self.hit_confirm,
            "graphic_size_x": self.graphic_size_x,
            "graphic_size_y": self.graphic_size_y,
            "graphic_adjust_x": self.graphic_adjust_x,
            "hit_count": self.hit_count,
            "last_hit_frame": self.last_hit_frame,
            "projectile_attack": [attack.to_dict() for attack in self.projectile_attack]
        }

    @classmethod
    def from_dict(cls, data_obj: dict):
        return CharacterData(
            player_number=data_obj["player_number"],
            hp=data_obj["hp"],
            energy=data_obj["energy"],
            x=data_obj["x"],
            y=data_obj["y"],
            left=data_obj["left"],
            right=data_obj["right"],
            top=data_obj["top"],
            bottom=data_obj["bottom"],
            speed_x=data_obj["speed_x"],
            speed_y=data_obj["speed_y"],
            state=State.from_int(data_obj["state"]),
            action=Action.from_int(data_obj["action"]),
            front=data_obj["front"],
            control=data_obj["control"],
            attack_data=AttackData.from_dict(data_obj["attack_data"]),
            remaining_frame=data_obj["remaining_frame"],
            hit_confirm=data_obj["hit_confirm"],
            graphic_size_x=data_obj["graphic_size_x"],
            graphic_size_y=data_obj["graphic_size_y"],
            graphic_adjust_x=data_obj["graphic_adjust_x"],
            hit_count=data_obj["hit_count"],
            last_hit_frame=data_obj["last_hit_frame"],
            projectile_attack=[AttackData.from_dict(attack) for attack in data_obj["projectile_attack"]]
        )
    
    @classmethod
    def from_proto(cls, proto_obj: Message):
        return CharacterData(
            player_number=proto_obj.player_number,
            hp=proto_obj.hp,
            energy=proto_obj.energy,
            x=proto_obj.x,
            y=proto_obj.y,
            left=proto_obj.left,
            right=proto_obj.right,
            top=proto_obj.top,
            bottom=proto_obj.bottom,
            speed_x=proto_obj.speed_x,
            speed_y=proto_obj.speed_y,
            state=State.from_int(proto_obj.state),
            action=Action.from_int(proto_obj.action),
            front=proto_obj.front,
            control=proto_obj.control,
            attack_data=AttackData.from_proto(proto_obj.attack_data),
            remaining_frame=proto_obj.remaining_frame,
            hit_confirm=proto_obj.hit_confirm,
            graphic_size_x=proto_obj.graphic_size_x,
            graphic_size_y=proto_obj.graphic_size_y,
            graphic_adjust_x=proto_obj.graphic_adjust_x,
            hit_count=proto_obj.hit_count,
            last_hit_frame=proto_obj.last_hit_frame,
            projectile_attack=[AttackData.from_proto(attack) for attack in proto_obj.projectile_attack]
        )

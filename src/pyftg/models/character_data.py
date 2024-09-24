from dataclasses import dataclass, field
from typing import List

from google.protobuf.message import Message

from pyftg.models.attack_data import AttackData
from pyftg.models.base_model import BaseModel
from pyftg.models.enums.action import Action
from pyftg.models.enums.state import State


@dataclass
class CharacterData(BaseModel):
    """
    CharacterData (BaseModel): Character data class.
    """

    player_number: bool = False
    """
    player_number (bool): The character side flag. True for player 1, False for player 2.
    """
    hp: int = 0
    """
    hp (int): The character's HP.
    """
    energy: int = 0
    """
    energy (int): The character's energy.
    """
    x: int = 0
    """
    x (int): The character graphic's center x-coordinate.
    """
    y: int = 0
    """
    y (int): The character graphic's center y-coordinate.
    """
    left: int = 0
    """
    left (int): The character's hit box's most-left x-coordinate.
    """
    right: int = 0
    """
    right (int): The character's hit box's most-right x-coordinate.
    """
    top: int = 0
    """
    top (int): The character's hit box's most-top y-coordinate.
    """
    bottom: int = 0
    """
    bottom (int): The character's hit box's most-bottom y-coordinate.
    """
    speed_x: int = 0
    """
    speed_x (int): The character's horizontal speed.
    """
    speed_y: int = 0
    """
    speed_y (int): The character's vertical speed.
    """
    state: State = State.STAND
    """
    state (State): The character's state: STAND / CROUCH / AIR / DOWN.
    """
    action: Action = Action.NEUTRAL
    """
    action (Action): The character's action.
    """
    front: bool = False
    """
    front (bool): The character's facing direction. True if facing right, otherwise False.
    """
    control: bool = False
    """
    control (bool): The flag whether this character can run a new motion with the motion's command.
    True if the character can run a new motion, otherwise False.
    """
    attack_data: AttackData = field(default_factory=AttackData)
    """
    attack_data (AttackData): The attack data that the character is using.
    """
    remaining_frame: int = 0
    """
    remaining_frame (int): The number of frames that the character needs to resume to its normal status.
    """
    hit_confirm: bool = False
    """
    hit_confirm (bool): The flag whether the motion hits the opponent or not.
    True if the motion hits the opponent, otherwise False.
    """
    graphic_size_x: int = 0
    """
    graphic_size_x (int): The character's graphic width.
    """
    graphic_size_y: int = 0
    """
    graphic_size_y (int): The character's graphic height.
    """
    graphic_adjust_x: int = 0
    """
    graphic_adjust_x (int): The amount of movement in the horizontal direction used to adjust the x-coordinate when determining the direction of the character.
    """
    hit_count: int = 0
    """
    hit_count (int): The continuous hit count of attacks used by this character.
    """
    last_hit_frame: int = 0
    """
    last_hit_frame (int): The frame number of the last frame that an attack used by this character hit the opponent.
    """
    projectile_attack: List[AttackData] = field(default_factory=lambda: [AttackData()] * 3)
    """
    projectile_attack (List[AttackData]): List of projectile attacks used by this character.
    """
    
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

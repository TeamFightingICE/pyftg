from dataclasses import dataclass, field

from google.protobuf.message import Message

from pyftg.models.base_model import BaseModel
from pyftg.models.hit_area import HitArea


@dataclass
class AttackData(BaseModel):
    setting_hit_area: HitArea = field(default_factory=HitArea)
    setting_speed_x: int = 0
    setting_speed_y: int = 0
    current_hit_area: HitArea = field(default_factory=HitArea)
    current_frame: int = 0
    player_number: bool = False
    speed_x: int = 0
    speed_y: int = 0
    start_up: int = 0
    active: int = 0
    hit_damage: int = 0
    guard_damage: int = 0
    start_add_energy: int = 0
    hit_add_energy: int = 0
    guard_add_energy: int = 0
    give_energy: int = 0
    impact_x: int = 0
    impact_y: int = 0
    give_guard_recov: int = 0
    attack_type: int = 0
    down_prop: bool = False
    is_projectile: bool = False
    is_live: bool = False
    empty_flag: bool = True
    identifier: str = ''
    
    def to_dict(self):
        return {
            "setting_hit_area": self.setting_hit_area.to_dict(),
            "setting_speed_x": self.setting_speed_x,
            "setting_speed_y": self.setting_speed_y,
            "current_hit_area": self.current_hit_area.to_dict(),
            "current_frame": self.current_frame,
            "player_number": self.player_number,
            "speed_x": self.speed_x,
            "speed_y": self.speed_y,
            "start_up": self.start_up,
            "active": self.active,
            "hit_damage": self.hit_damage,
            "guard_damage": self.guard_damage,
            "start_add_energy": self.start_add_energy,
            "hit_add_energy": self.hit_add_energy,
            "guard_add_energy": self.guard_add_energy,
            "give_energy": self.give_energy,
            "impact_x": self.impact_x,
            "impact_y": self.impact_y,
            "give_guard_recov": self.give_guard_recov,
            "attack_type": self.attack_type,
            "down_prop": self.down_prop,
            "is_projectile": self.is_projectile,
            "is_live": self.is_live,
            "empty_flag": self.empty_flag,
            "identifier": self.identifier
        }

    @classmethod
    def from_dict(cls, data_obj: dict):
        return AttackData(
            setting_hit_area=HitArea.from_dict(data_obj["setting_hit_area"]),
            setting_speed_x=data_obj["setting_speed_x"],
            setting_speed_y=data_obj["setting_speed_y"],
            current_hit_area=HitArea.from_dict(data_obj["current_hit_area"]),
            current_frame=data_obj["current_frame"],
            player_number=data_obj["player_number"],
            speed_x=data_obj["speed_x"],
            speed_y=data_obj["speed_y"],
            start_up=data_obj["start_up"],
            active=data_obj["active"],
            hit_damage=data_obj["hit_damage"],
            guard_damage=data_obj["guard_damage"],
            start_add_energy=data_obj["start_add_energy"],
            hit_add_energy=data_obj["hit_add_energy"],
            guard_add_energy=data_obj["guard_add_energy"],
            give_energy=data_obj["give_energy"],
            impact_x=data_obj["impact_x"],
            impact_y=data_obj["impact_y"],
            give_guard_recov=data_obj["give_guard_recov"],
            attack_type=data_obj["attack_type"],
            down_prop=data_obj["down_prop"],
            is_projectile=data_obj["is_projectile"],
            is_live=data_obj["is_live"],
            empty_flag=data_obj["empty_flag"],
            identifier=data_obj["identifier"]
        )
    
    @classmethod
    def from_proto(cls, proto_obj: Message):
        return AttackData(
            setting_hit_area=HitArea.from_proto(proto_obj.setting_hit_area),
            setting_speed_x=proto_obj.setting_speed_x,
            setting_speed_y=proto_obj.setting_speed_y,
            current_hit_area=HitArea.from_proto(proto_obj.current_hit_area),
            current_frame=proto_obj.current_frame,
            player_number=proto_obj.player_number,
            speed_x=proto_obj.speed_x,
            speed_y=proto_obj.speed_y,
            start_up=proto_obj.start_up,
            active=proto_obj.active,
            hit_damage=proto_obj.hit_damage,
            guard_damage=proto_obj.guard_damage,
            start_add_energy=proto_obj.start_add_energy,
            hit_add_energy=proto_obj.hit_add_energy,
            guard_add_energy=proto_obj.guard_add_energy,
            give_energy=proto_obj.give_energy,
            impact_x=proto_obj.impact_x,
            impact_y=proto_obj.impact_y,
            give_guard_recov=proto_obj.give_guard_recov,
            attack_type=proto_obj.attack_type,
            down_prop=proto_obj.down_prop,
            is_projectile=proto_obj.is_projectile,
            is_live=proto_obj.is_live,
            empty_flag=proto_obj.empty_flag,
            identifier=proto_obj.identifier
        )

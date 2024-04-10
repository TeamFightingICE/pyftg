from dataclasses import dataclass

from google.protobuf.message import Message

from pyftg.models.base_model import BaseModel
from pyftg.models.hit_area import HitArea


@dataclass
class AttackData(BaseModel):
    setting_hit_area: HitArea
    setting_speed_x: int
    setting_speed_y: int
    current_hit_area: HitArea
    current_frame: int
    player_number: bool
    speed_x: int
    speed_y: int
    start_up: int
    active: int
    hit_damage: int
    guard_damage: int
    start_add_energy: int
    hit_add_energy: int
    guard_add_energy: int
    give_energy: int
    impact_x: int
    impact_y: int
    give_guard_recov: int
    attack_type: int
    down_prop: bool
    is_projectile: bool
    
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
            "is_projectile": self.is_projectile
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
            is_projectile=data_obj["is_projectile"]
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
        )
    
    @classmethod
    def get_default_instance(cls):
        return AttackData(
            setting_hit_area=HitArea.get_default_instance(), setting_speed_x=0, setting_speed_y=0,
            current_hit_area=HitArea.get_default_instance(), current_frame=0, player_number=False,
            speed_x=0, speed_y=0, start_up=0, active=0, hit_damage=0, guard_damage=0,
            start_add_energy=0, hit_add_energy=0, guard_add_energy=0, give_energy=0,
            impact_x=0, impact_y=0, give_guard_recov=0, attack_type=0, down_prop=False, is_projectile=False
        )

from .hit_area import HitArea

class AttackData:
    def __init__(self, attack_data):
        self.setting_hit_area = HitArea(attack_data.setting_hit_area)
        self.setting_speed_x: int = attack_data.setting_speed_x
        self.setting_speed_y: int = attack_data.setting_speed_y
        self.current_hit_area = HitArea(attack_data.current_hit_area)
        self.current_frame: int = attack_data.current_frame
        self.player_number: bool = attack_data.player_number
        self.speed_x: int = attack_data.speed_x
        self.speed_y: int = attack_data.speed_y
        self.start_up: int = attack_data.start_up
        self.active: int = attack_data.active
        self.hit_damage: int = attack_data.hit_damage
        self.guard_damage: int = attack_data.guard_damage
        self.start_add_energy: int = attack_data.start_add_energy
        self.hit_add_energy: int = attack_data.hit_add_energy
        self.guard_add_energy: int = attack_data.guard_add_energy
        self.give_energy: int = attack_data.give_energy
        self.impact_x: int = attack_data.impact_x
        self.impact_y: int = attack_data.impact_y
        self.give_guard_recov: int = attack_data.give_guard_recov
        self.attack_type: int = attack_data.attack_type
        self.down_prop: bool = attack_data.down_prop
        self.is_projectile: bool = attack_data.is_projectile

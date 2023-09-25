from .attack_data import AttackData
from .character_data import CharacterData
import numpy as np

class FrameData:
    def __init__(self, frame_data=None):
        if not frame_data:
            self.character_data = [None, None]
            self.current_frame_number = -1
            self.current_round = -1
            self.projectile_data = []
            self.empty_flag = True
            self.front = [False, False]
        else:
            self.character_data = [CharacterData(x) for x in frame_data.character_data]
            self.current_frame_number: int = frame_data.current_frame_number
            self.current_round: int = frame_data.current_round
            self.projectile_data = [AttackData(x) for x in frame_data.projectile_data]
            self.empty_flag: bool = frame_data.empty_flag
            self.front = [bool(x) for x in frame_data.front]

    def is_front(self, player: bool):
        return self.front[0 if player else 1]
    
    def get_character(self, player: bool):
        return self.character_data[0 if player else 1]
    
    def get_projectiles_by_player(self, player: bool):
        return [x for x in self.projectile_data if x.player_number == player]

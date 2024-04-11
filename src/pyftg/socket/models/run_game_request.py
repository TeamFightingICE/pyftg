from dataclasses import dataclass

from pyftg.models.base_model import BaseModel


@dataclass
class RunGameRequest(BaseModel):
    character_1: str
    character_2: str
    player_1: str
    player_2: str
    game_number: int

    def to_dict(self) -> dict:
        return {
            'character_1': self.character_1,
            'character_2': self.character_2,
            'player_1': self.player_1,
            'player_2': self.player_2,
            'game_number': self.game_number,
        }
    
    @classmethod
    def from_dict(cls, data_obj: dict):
        return RunGameRequest(
            character_1=data_obj['character_1'],
            character_2=data_obj['character_2'],
            player_1=data_obj['player_1'],
            player_2=data_obj['player_2'],
            game_number=data_obj['game_number'],
        )
    
    @classmethod
    def get_default_instance(cls):
        return RunGameRequest(
            character_1='',
            character_2='',
            player_1='',
            player_2='',
            game_number=0,
        )

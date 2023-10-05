import numpy as np

class GameData:
    def __init__(self, game_data):
        self.max_hps = np.array(game_data.max_hps, dtype=np.int32)
        self.max_energies = np.array(game_data.max_energies, dtype=np.int32)
        self.character_names = (game_data.character_names[0], game_data.character_names[1])
        self.ai_names = (game_data.ai_names[0], game_data.ai_names[1])

    def get_character_name(self, player: bool) -> str:
        return self.character_names[0 if player else 1]
    
    def get_ai_name(self, player: bool) -> str:
        return self.ai_names[0 if player else 1]

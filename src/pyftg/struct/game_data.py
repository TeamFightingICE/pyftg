class GameData:
    def __init__(self, game_data):
        self.max_hps = [int(x) for x in game_data.max_hps]
        self.max_energies = [int(x) for x in game_data.max_energies]
        self.character_names = [game_data.character_names[0], game_data.character_names[1]]
        self.ai_names = [game_data.ai_names[0], game_data.ai_names[1]]

    def get_character_name(self, player: bool) -> str:
        return self.character_names[0 if player else 1]
    
    def get_ai_name(self, player: bool) -> str:
        return self.ai_names[0 if player else 1]

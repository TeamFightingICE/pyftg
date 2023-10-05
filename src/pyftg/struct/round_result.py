import numpy as np

class RoundResult:
    def __init__(self, round_result):
        self.current_round = round_result.current_round
        self.remaining_hps = [int(x) for x in round_result.remaining_hps]
        self.elapsed_frame = round_result.elapsed_frame

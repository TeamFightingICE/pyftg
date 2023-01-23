import numpy as np

class RoundResult:
    def __init__(self, round_result):
        self.current_round = round_result.current_round
        self.remaining_hps = np.array(round_result.remaining_hps, dtype=np.int32)
        self.elapsed_frame = round_result.elapsed_frame

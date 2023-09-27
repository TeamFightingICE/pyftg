from pyftg.struct import GameData, FrameData, ScreenData, AudioData, RoundResult
from pyftg import ObserverHandler
from enum import Enum
from PIL import Image
import io
import os
import gzip
import logging
import json
import datetime
import numpy as np

def todict(obj, classkey=None):
    if isinstance(obj, dict):
        data = {}
        for (k, v) in obj.items():
            data[k] = todict(v, classkey)
        return data
    elif isinstance(obj, Enum):
        return str(obj)
    elif hasattr(obj, "_ast"):
        return todict(obj._ast())
    elif hasattr(obj, "__iter__") and not isinstance(obj, str):
        return [todict(v, classkey) for v in obj]
    elif hasattr(obj, "__dict__"):
        data = dict([(key, todict(value, classkey)) 
            for key, value in obj.__dict__.items() 
            if not callable(value) and not key.startswith('_')])
        if classkey is not None and hasattr(obj, "__class__"):
            data[classkey] = obj.__class__.__name__
        return data
    else:
        return obj

class Collector(ObserverHandler):
    def __init__(self) -> None:
        self.frames = list()
        self.counter = 0

    def on_initialize(self, game: GameData):
        logging.info('initialize')
        self.game_data = game
        self.change_directory()

    def on_game_update(self, frame_data: FrameData, screen_data: ScreenData, audio_data: AudioData):
        logging.info('round number: %s', frame_data.current_frame_number)

        img = np.reshape(bytearray(screen_data.display_bytes), (640, 960, 3))
        img = np.flipud(img)
        img = Image.fromarray(img)
        img.save('{}/images/{:03d}.png'.format(self.path, self.counter))

        self.frames.append(todict(frame_data))
        self.counter += 1

    def on_round_end(self, round_result: RoundResult, is_game_end: bool):
        logging.info('round end: %s', round_result.elapsed_frame)

        with open('{}/game_log.json'.format(self.path), 'w') as file:
            file.write(json.dumps(self.frames, indent=2))

        with open('{}/result.json'.format(self.path), 'w') as file:
            file.write(json.dumps(todict(round_result), indent=2))
        
        self.frames.clear()
        if not is_game_end:
            self.change_directory()

    def change_directory(self):
        current_datetime = datetime.datetime.now()
        formatted_datetime = current_datetime.strftime("%Y.%m.%d-%H.%M.%S")
        self.counter = 0
        self.path = 'Collector/{}'.format(formatted_datetime)

        os.mkdir(self.path)
        os.mkdir('{}/images'.format(self.path))

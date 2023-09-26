import logging
import argparse
import io
import cv2
import gzip
import numpy as np

from pyftg import ObserverGateway, ObserverHandler
from pyftg.enum import DataFlag
from pyftg.struct import AudioData, FrameData, GameData, RoundResult, ScreenData

class Handler(ObserverHandler):
    def on_initialize(self, game: GameData):
        logging.info('initialize')
    
    def on_game_update(self, frame: FrameData, screen: ScreenData, audio: AudioData):
        compressed_display_bytes = io.BytesIO(screen.display_bytes)
        with gzip.GzipFile(fileobj=compressed_display_bytes, mode='rb') as file:
            decompressed_display_bytes = file.read()
        img = np.reshape(bytearray(decompressed_display_bytes), (640, 960, 3))
        img = np.flipud(img)
        cv2.imshow('OpenCV', cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
        cv2.waitKey(1)
    
    def on_round_end(self, result: RoundResult, game_end_flag: bool):
        logging.info('round end')
        cv2.destroyAllWindows()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=50051, type=int, help='Port used by DareFightingICE')
    args = parser.parse_args()
    logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', level=logging.DEBUG)
    gateway = ObserverGateway(handler=Handler(), data_flag=DataFlag.SCREEN_DATA, interval=1, port=args.port)
    logging.info('Observer is started.')
    gateway.start()
    gateway.close()

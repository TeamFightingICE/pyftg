import logging
import socket
from threading import Thread

import orjson

from pyftg.aiinterface.ai_interface import AIInterface
from pyftg.models.audio_data import AudioData
from pyftg.models.frame_data import FrameData
from pyftg.models.game_data import GameData
from pyftg.models.round_result import RoundResult
from pyftg.models.screen_data import ScreenData

logger = logging.getLogger(__name__)

CLOSE = b'\x00'
INITIALIZE = b'\x01'
PROCESSING = b'\x02'
ROUND_END = b'\x03'
GAME_END = b'\x04'


class AIController(Thread):
    def __init__(self, host: str, port: int, ai: AIInterface, player_number: bool):
        Thread.__init__(self)
        self.host = host
        self.port = port
        self.ai = ai
        self.player_number = player_number
    
    def initialize_socket(self) -> str:
        # Send player number (b'\x00' is player 1, b'\x01' is player 2)
        self.client.send((not self.player_number).to_bytes(1, byteorder='little', signed=False))

    def recv_data(self) -> bytes:
        header_data = self.client.recv(4)
        buffer_size = int.from_bytes(header_data, byteorder='little')
        body_data = self.client.recv(buffer_size)
        return body_data
    
    def send_data(self, data: bytes):
        buffer_size = len(data).to_bytes(4, byteorder='little')
        self.client.send(buffer_size)
        self.client.send(data)

    def on_initialize(self):
        game_data = GameData.from_dict(orjson.loads(self.recv_data()))
        player_number = True if self.client.recv(1) == b'\x01' else False
        self.ai.initialize(game_data, player_number)

    def on_processing(self):
        is_control = bool(self.client.recv(1))
        frame_data = FrameData.from_dict(orjson.loads(self.recv_data()))
        audio_data = AudioData.from_dict(orjson.loads(self.recv_data()))
        screen_data = ScreenData.from_dict(orjson.loads(self.recv_data()), decompress=True)

        self.ai.get_information(frame_data, is_control)
        self.ai.get_screen_data(screen_data)
        self.ai.get_audio_data(audio_data)

        self.ai.processing()
        self.send_data(self.ai.input().to_json())

    def on_round_end(self):
        round_result = RoundResult.from_dict(orjson.loads(self.recv_data()))
        self.ai.round_end(round_result)

    def run(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, self.port))
        self.initialize_socket()
        while True:
            data = self.client.recv(1)
            if not data or data == CLOSE:
                break
            elif data == INITIALIZE:
                self.on_initialize()
            elif data == PROCESSING:
                self.on_processing()
            elif data == ROUND_END:
                self.on_round_end()
            elif data == GAME_END:
                self.on_round_end()
                self.ai.game_end()
            else:
                logger.error(f"Unknown data: {data}")
                break
    
    def close(self):
        self.client.close()

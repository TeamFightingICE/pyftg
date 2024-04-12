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
    
    def initialize_socket(self) -> None:
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, self.port))
        self.send_data(self.player_number.to_bytes(1, byteorder='little', signed=False), with_header=False)
        self.send_data(self.ai.is_blind().to_bytes(1, byteorder='little', signed=False), with_header=False)

    def recv_data(self, n: int = -1) -> bytes:
        if n == -1:
            header_data = self.client.recv(4)
            n = int.from_bytes(header_data, byteorder='little')
            if n == 0:
                return None
        body_data = self.client.recv(n)
        return body_data
    
    def send_data(self, data: bytes, with_header: bool = True) -> None:
        if with_header:
            buffer_size = len(data).to_bytes(4, byteorder='little')
            self.client.send(buffer_size)
        self.client.send(data)

    def on_initialize(self) -> None:
        game_data_packet = self.recv_data()
        player_number_packet = self.recv_data(1)

        game_data = GameData.from_dict(orjson.loads(game_data_packet))
        player_number = player_number_packet == b'\x01'

        self.ai.initialize(game_data, player_number)

    def on_processing(self) -> None:
        is_control = bool(self.client.recv(1))

        non_delay_frame_data_packet = self.recv_data()
        frame_data_packet = self.recv_data()
        audio_data_packet = self.recv_data()
        screen_data_packet = self.recv_data()
        screen_data_packet = self.recv_data()

        if non_delay_frame_data_packet:
            self.ai.get_non_delay_frame_data(FrameData.from_dict(orjson.loads(non_delay_frame_data_packet)))

        if screen_data_packet:
            self.ai.get_screen_data(ScreenData.from_dict(orjson.loads(screen_data_packet), decompress=True))

        self.ai.get_information(FrameData.from_dict(orjson.loads(frame_data_packet)), is_control)
        self.ai.get_audio_data(AudioData.from_dict(orjson.loads(audio_data_packet)))

        self.ai.processing()
        self.send_data(self.ai.input().to_json())

    def on_round_end(self) -> None:
        round_result_packet = self.recv_data()

        round_result = RoundResult.from_dict(orjson.loads(round_result_packet))
        self.ai.round_end(round_result)

    def run(self):
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

import logging
import socket
from threading import Thread

from google.protobuf.message import Message

from pyftg.aiinterface.ai_interface import AIInterface
from pyftg.models.audio_data import AudioData
from pyftg.models.enums.flag import Flag
from pyftg.models.frame_data import FrameData
from pyftg.models.game_data import GameData
from pyftg.models.key import Key
from pyftg.models.round_result import RoundResult
from pyftg.models.screen_data import ScreenData
from pyftg.protoc import service_pb2
from pyftg.socket.utils.threading import recv_data, send_data
from pyftg.utils.protobuf import convert_key_to_proto

logger = logging.getLogger(__name__)

CLOSE = b'\x00'
PROCESSING = b'\x01'


class AIController(Thread):
    def __init__(self, host: str, port: int, ai: AIInterface, player_number: bool):
        Thread.__init__(self)
        self.host = host
        self.port = port
        self.ai = ai
        self.player_number = player_number
    
    def initialize(self) -> None:
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, self.port))
        request: Message = service_pb2.InitializeRequest(player_number=self.player_number, player_name=self.ai.name(), is_blind=self.ai.is_blind())
        send_data(self.client, b'\x01', with_header=False)  # 1: Initialize
        send_data(self.client, request.SerializeToString())

    def send_input_key(self, key: Key) -> None:
        proto_key = convert_key_to_proto(key)
        send_data(self.client, proto_key.SerializeToString())

    def run(self):
        self.initialize()
        while True:
            data = self.client.recv(1)
            if not data or data == CLOSE:
                break
            elif data == PROCESSING:
                state_packet = recv_data(self.client)
                state: Message = service_pb2.PlayerGameState()
                state.ParseFromString(state_packet)

                flag = Flag(state.state_flag)
                if flag is Flag.INITIALIZE:
                    self.ai.initialize(GameData.from_proto(state.game_data), self.player_number)
                elif flag is Flag.PROCESSING:
                    if state.HasField("non_delay_frame_data"):
                        self.ai.get_non_delay_frame_data(FrameData.from_proto(state.non_delay_frame_data))

                    if state.HasField("screen_data"):
                        self.ai.get_screen_data(ScreenData.from_proto(state.screen_data))

                    self.ai.get_information(FrameData.from_proto(state.frame_data), state.is_control)
                    self.ai.get_audio_data(AudioData.from_proto(state.audio_data))
                    
                    self.ai.processing()
                    self.send_input_key(self.ai.input())
                elif flag is Flag.ROUND_END:
                    self.ai.round_end(RoundResult.from_proto(state.round_result))
                elif flag is Flag.GAME_END:
                    self.ai.round_end(RoundResult.from_proto(state.round_result))
                    self.ai.game_end()
    
    def close(self):
        self.client.close()

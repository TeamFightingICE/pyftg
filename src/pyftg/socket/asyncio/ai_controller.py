import asyncio
import logging

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
from pyftg.socket.utils.asyncio import recv_data, send_data
from pyftg.utils.protobuf import convert_key_to_proto

logger = logging.getLogger(__name__)

CLOSE = b'\x00'
PROCESSING = b'\x01'


class AIController:
    def __init__(self, host: str, port: int, ai: AIInterface, player_number: bool):
        self.host = host
        self.port = port
        self.ai = ai
        self.player_number = player_number
    
    async def initialize(self) -> None:
        self.reader, self.writer = await asyncio.open_connection(self.host, self.port)
        request: Message = service_pb2.InitializeRequest(player_number=self.player_number, player_name=self.ai.name(), is_blind=self.ai.is_blind())
        await send_data(self.writer, b'\x01', with_header=False)  # 1: Initialize
        await send_data(self.writer, request.SerializeToString())

    async def send_input_key(self, key: Key) -> None:
        proto_key = convert_key_to_proto(key)
        await send_data(self.writer, proto_key.SerializeToString())

    async def run(self):
        await self.initialize()
        while True:
            data = await recv_data(self.reader, 1)
            if not data or data == CLOSE:
                break
            elif data == PROCESSING:
                state_packet = await recv_data(self.reader)
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

                    loop = asyncio.get_event_loop()
                    await loop.run_in_executor(None, self.ai.processing)
                    await self.send_input_key(self.ai.input())
                elif flag is Flag.ROUND_END:
                    self.ai.round_end(RoundResult.from_proto(state.round_result))
                elif flag is Flag.GAME_END:
                    self.ai.round_end(RoundResult.from_proto(state.round_result))
                    self.ai.game_end()
        self.ai.close()
        self.writer.close()
        await self.writer.wait_closed()

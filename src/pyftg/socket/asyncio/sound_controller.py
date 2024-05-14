import asyncio
import logging
import time

from google.protobuf.message import Message

from pyftg.aiinterface.soundgenai_interface import SoundGenAIInterface
from pyftg.models.enums.flag import Flag
from pyftg.models.frame_data import FrameData
from pyftg.models.game_data import GameData
from pyftg.models.key import Key
from pyftg.models.round_result import RoundResult
from pyftg.protoc import service_pb2
from pyftg.socket.utils.asyncio import recv_data, send_data
from pyftg.utils.protobuf import convert_key_to_proto

logger = logging.getLogger(__name__)

CLOSE = b'\x00'
PROCESSING = b'\x01'
INIT_SOUND_GENAI = b'\x03'


class SoundController:
    def __init__(self, host: str, port: int, sound_ai: SoundGenAIInterface):
        self.host = host
        self.port = port
        self.sound_ai = sound_ai

    async def initialize(self):
        self.reader, self.writer = await asyncio.open_connection(self.host, self.port)
        request: Message = service_pb2.InitializeRequest(player_number=True, player_name="Sound", is_blind=True)
        await send_data(self.writer, INIT_SOUND_GENAI, with_header=False)
        await send_data(self.writer, request.SerializeToString())

    async def send_audio_sample(self, audio_sample: bytes) -> None:
        await send_data(self.writer, audio_sample)

    async def run(self):
        await self.initialize()
        while True:
            data = await recv_data(self.reader, 1)
            if not data or data == CLOSE:
                break
            elif data == PROCESSING:
                start = time.perf_counter_ns()
                state_packet = await recv_data(self.reader)
                state: Message = service_pb2.PlayerGameState()
                state.ParseFromString(state_packet)
                end = time.perf_counter_ns()
                print("processing time:", (end - start) / 1e6, "ms")

                flag = Flag(state.state_flag)
                if flag is Flag.INITIALIZE:
                    self.sound_ai.initialize(GameData.from_proto(state.game_data))
                elif flag is Flag.PROCESSING:
                    self.sound_ai.get_information(FrameData.from_proto(state.frame_data))
                    
                    self.sound_ai.processing()
                    await self.send_audio_sample(self.sound_ai.audio_sample())
                elif flag is Flag.ROUND_END:
                    self.sound_ai.round_end(RoundResult.from_proto(state.round_result))
                elif flag is Flag.GAME_END:
                    self.sound_ai.round_end(RoundResult.from_proto(state.round_result))
                    self.sound_ai.game_end()

    async def close(self):
        self.sound_ai.close()
        self.writer.close()
        await self.writer.wait_closed()

import asyncio
import logging

from google.protobuf.message import Message

from pyftg.aiinterface.soundgenai_interface import SoundGenAIInterface
from pyftg.models.enums.flag import Flag
from pyftg.models.frame_data import FrameData
from pyftg.models.game_data import GameData
from pyftg.models.round_result import RoundResult
from pyftg.protoc import service_pb2
from pyftg.socket.utils.asyncio import recv_data, send_data

logger = logging.getLogger(__name__)

CLOSE = b'\x00'
PROCESSING = b'\x01'
INIT_SOUND_GENAI = b'\x03'


class GenerativeSoundGateway:
    def __init__(self, host='127.0.0.1', port=50051):
        self.host = host
        self.port = port
        self.cancelled = False
        self.sound_ai: SoundGenAIInterface = None

    def register(self, sound_ai: SoundGenAIInterface) -> None:
        self.sound_ai = sound_ai

    async def initialize(self):
        self.reader, self.writer = await asyncio.open_connection(self.host, self.port)
        await send_data(self.writer, INIT_SOUND_GENAI, with_header=False)
        logger.info(f'Connected to DareFightingICE at {self.host}:{self.port}')

    async def run(self):
        if not self.sound_ai:
            raise ValueError('Sound AI is not registered')

        await self.initialize()

        while not self.cancelled:
            data = await recv_data(self.reader, 1)
            if not data or data == CLOSE:
                self.cancelled = True
                logger.info('Connection closed by DareFightingICE')
            elif data == PROCESSING:
                state_bytes = await recv_data(self.reader)
                state_proto: Message = service_pb2.SpectatorGameState()
                state_proto.ParseFromString(state_bytes)
                
                flag = Flag(state_proto.state_flag)
                if flag is Flag.INITIALIZE:
                    self.sound_ai.initialize(GameData.from_proto(state_proto.game_data))
                elif flag is Flag.INIT_ROUND:
                    self.sound_ai.init_round()
                elif flag is Flag.PROCESSING:
                    self.sound_ai.processing_game(FrameData.from_proto(state_proto.frame_data))
                    audio_data_bytes = self.sound_ai.audio_sample()
                    await send_data(self.writer, audio_data_bytes)
                elif flag is Flag.ROUND_END:
                    self.sound_ai.round_end(RoundResult.from_proto(state_proto.round_result))
                elif flag is Flag.GAME_END:
                    self.sound_ai.game_end()

    async def close(self):
        self.sound_ai.close()
        self.writer.close()
        await self.writer.wait_closed()

import asyncio
import logging

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


class AIController:
    def __init__(self, host: str, port: int, ai: AIInterface, player_number: bool):
        self.host = host
        self.port = port
        self.ai = ai
        self.player_number = player_number
    
    async def initialize_socket(self) -> str:
        await self.send_data(self.player_number.to_bytes(1, byteorder='little', signed=False), with_header=False)
        await self.send_data(self.ai.is_blind().to_bytes(1, byteorder='little', signed=False), with_header=False)

    async def recv_data(self, n: int = -1) -> bytes:
        if n == -1:
            header_data = await self.reader.read(4)
            n = int.from_bytes(header_data, byteorder='little')
            if n == 0:
                return None
        body_data = await self.reader.read(n)
        return body_data
    
    async def send_data(self, data: bytes, with_header: bool = True):
        if with_header:
            buffer_size = len(data).to_bytes(4, byteorder='little')
            self.writer.write(buffer_size)
            await self.writer.drain()
        self.writer.write(data)
        await self.writer.drain()

    async def on_initialize(self):
        game_data = GameData.from_dict(orjson.loads(await self.recv_data()))
        player_number = True if await self.recv_data(1) == b'\x01' else False
        self.ai.initialize(game_data, player_number)

    async def on_processing(self):
        is_control = bool(await self.recv_data(1))

        non_delay_frame_data_packet = await self.recv_data()
        if non_delay_frame_data_packet:
            self.ai.get_non_delay_frame_data(FrameData.from_dict(orjson.loads(non_delay_frame_data_packet)))

        self.ai.get_information(FrameData.from_dict(orjson.loads(await self.recv_data())), is_control)
        self.ai.get_audio_data(AudioData.from_dict(orjson.loads(await self.recv_data())))

        screen_data_packet = await self.recv_data()
        if screen_data_packet:
            self.ai.get_screen_data(ScreenData.from_dict(orjson.loads(screen_data_packet)))

        self.ai.processing()
        await self.send_data(self.ai.input().to_json())

    async def on_round_end(self):
        round_result = RoundResult.from_dict(orjson.loads(await self.recv_data()))
        self.ai.round_end(round_result)

    async def run(self):
        self.reader, self.writer = await asyncio.open_connection(self.host, self.port)
        await self.initialize_socket()
        while True:
            data = await self.reader.read(1)
            if not data or data == CLOSE:
                break
            elif data == INITIALIZE:
                await self.on_initialize()
            elif data == PROCESSING:
                await self.on_processing()
            elif data == ROUND_END:
                await self.on_round_end()
            elif data == GAME_END:
                await self.on_round_end()
                self.ai.game_end()
            else:
                logger.error(f"Unknown data: {data}")
                break
        
    async def close(self):
        self.writer.close()
        await self.writer.wait_closed()

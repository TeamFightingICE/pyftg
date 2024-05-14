import asyncio
import logging

from google.protobuf.message import Message

from pyftg.aiinterface.stream_interface import StreamInterface
from pyftg.models.audio_data import AudioData
from pyftg.models.enums.flag import Flag
from pyftg.models.frame_data import FrameData
from pyftg.models.game_data import GameData
from pyftg.models.round_result import RoundResult
from pyftg.models.screen_data import ScreenData
from pyftg.protoc import service_pb2
from pyftg.socket.utils.asyncio import recv_data, send_data

logger = logging.getLogger(__name__)

CLOSE = b'\x00'
PROCESSING = b'\x01'
INIT_STREAM = b'\x04'


class StreamController:
    def __init__(self, host: str, port: int, stream: StreamInterface):
        self.host = host
        self.port = port
        self.stream = stream
    
    async def initialize(self) -> None:
        self.reader, self.writer = await asyncio.open_connection(self.host, self.port)
        await send_data(self.writer, INIT_STREAM, with_header=False)

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
                    self.stream.initialize(GameData.from_proto(state.game_data))
                elif flag is Flag.PROCESSING:
                    self.stream.get_information(FrameData.from_proto(state.frame_data))
                    self.stream.get_audio_data(AudioData.from_proto(state.audio_data))
                    self.stream.get_screen_data(ScreenData.from_proto(state.screen_data))
                    
                    self.stream.processing()
                elif flag is Flag.ROUND_END:
                    self.stream.round_end(RoundResult.from_proto(state.round_result))
                elif flag is Flag.GAME_END:
                    self.stream.round_end(RoundResult.from_proto(state.round_result))
                    self.stream.game_end()
        
    async def close(self):
        self.writer.close()
        await self.writer.wait_closed()

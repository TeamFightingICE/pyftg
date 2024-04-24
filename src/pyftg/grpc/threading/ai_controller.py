import logging
from threading import Thread
from typing import Generator

from google.protobuf.message import Message

from pyftg.aiinterface.ai_interface import AIInterface
from pyftg.models.audio_data import AudioData
from pyftg.models.enums.flag import Flag
from pyftg.models.frame_data import FrameData
from pyftg.models.game_data import GameData
from pyftg.models.key import Key
from pyftg.models.round_result import RoundResult
from pyftg.models.screen_data import ScreenData
from pyftg.protoc import service_pb2, service_pb2_grpc
from pyftg.utils.protobuf import convert_key_to_proto

logger = logging.getLogger(__name__)


class AIController(Thread):
    def __init__(self, stub: service_pb2_grpc.ServiceStub, ai: AIInterface, player_number: bool):
        Thread.__init__(self)
        self.stub = stub
        self.ai = ai
        self.player_number = player_number
    
    def initialize_rpc(self) -> str:
        request = service_pb2.InitializeRequest(player_number=self.player_number, player_name=self.ai.name(), is_blind=self.ai.is_blind())
        response = self.stub.Initialize(request)
        return response.player_uuid

    def participate_rpc(self, player_uuid: str) -> Generator[Message, None, None]:
        request = service_pb2.ParticipateRequest(player_uuid=player_uuid)
        return self.stub.Participate(request)
    
    def input_rpc(self, player_uuid: str, key: Key) -> None:
        proto_key = convert_key_to_proto(key)
        self.stub.Input(service_pb2.PlayerInput(player_uuid=player_uuid, input_key=proto_key))
    
    def run(self):
        player_uuid = self.initialize_rpc()
        for state in self.participate_rpc(player_uuid):
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
                self.input_rpc(player_uuid, self.ai.input())
            elif flag is Flag.ROUND_END:
                self.ai.round_end(RoundResult.from_proto(state.round_result))
            elif flag is Flag.GAME_END:
                self.ai.round_end(RoundResult.from_proto(state.round_result))
                self.ai.game_end()

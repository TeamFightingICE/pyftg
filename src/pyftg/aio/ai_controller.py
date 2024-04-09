from pyftg.aiinterface import AIInterface
from pyftg.models.audio_data import AudioData
from pyftg.models.enums.flag import Flag
from pyftg.models.frame_data import FrameData
from pyftg.models.game_data import GameData
from pyftg.models.key import Key
from pyftg.models.round_result import RoundResult
from pyftg.models.screen_data import ScreenData
from pyftg.protoc import message_pb2, service_pb2, service_pb2_grpc


class AIController():
    def __init__(self, stub: service_pb2_grpc.ServiceStub, ai: AIInterface, player_number: bool):
        self.stub = stub
        self.ai = ai
        self.player_number = player_number
    
    async def initialize_rpc(self):
        request = service_pb2.InitializeRequest(player_number=self.player_number, player_name=self.ai.name(), is_blind=self.ai.is_blind())
        response = await self.stub.Initialize(request)
        self.player_uuid: str = response.player_uuid

    async def participate_rpc(self):
        request = service_pb2.ParticipateRequest(player_uuid=self.player_uuid)
        return self.stub.Participate(request)
    
    async def input_rpc(self, key: Key):
        grpc_key = message_pb2.GrpcKey(A=key.A, B=key.B, C=key.C, U=key.U, D=key.D, L=key.L, R=key.R)
        await self.stub.Input(service_pb2.PlayerInput(player_uuid=self.player_uuid, input_key=grpc_key))
    
    async def run(self):
        await self.initialize_rpc()
        async for state in await self.participate_rpc():
            flag = Flag(state.state_flag)
            if flag is Flag.INITIALIZE:
                self.ai.initialize(GameData.from_proto(state.game_data), self.player_number)
            elif flag is Flag.PROCESSING:
                if state.HasField("non_delay_frame_data"):
                    self.ai.get_non_delay_frame_data(FrameData.from_proto(state.non_delay_frame_data))

                self.ai.get_information(FrameData.from_proto(state.frame_data), state.is_control)

                if state.HasField("screen_data"):
                    self.ai.get_screen_data(ScreenData.from_proto(state.screen_data))

                if state.HasField("audio_data"):
                    self.ai.get_audio_data(AudioData.from_proto(state.audio_data))
                    
                self.ai.processing()
                await self.input_rpc(self.ai.input())
            elif flag is Flag.ROUND_END:
                self.ai.round_end(RoundResult.from_proto(state.round_result))
            elif flag is Flag.GAME_END:
                self.ai.round_end(RoundResult.from_proto(state.round_result))
                self.ai.game_end()

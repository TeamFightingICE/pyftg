import grpc

from pyftg.grpc.threading.observer_handler import ObserverHandler
from pyftg.models.audio_data import AudioData
from pyftg.models.enums.data_flag import DataFlag
from pyftg.models.enums.flag import Flag
from pyftg.models.frame_data import FrameData
from pyftg.models.game_data import GameData
from pyftg.models.round_result import RoundResult
from pyftg.models.screen_data import ScreenData
from pyftg.protoc import service_pb2, service_pb2_grpc


class ObserverGateway:
    def __init__(self, handler: ObserverHandler, data_flag: DataFlag, interval=1, host='127.0.0.1', port=50051):
        self.host = host
        self.port = port
        self.channel = grpc.insecure_channel(
            target=f"{host}:{port}",
            compression=grpc.Compression.Gzip,
        )
        self.stub = service_pb2_grpc.ServiceStub(self.channel)
        self.handler = handler
        self.interval = interval
        self.data_flag = data_flag

    def spectate_rpc(self):
        frame_data_flag = False
        screen_data_flag = False
        audio_data_flag = False

        if self.data_flag == DataFlag.ALL:
            frame_data_flag = True
            screen_data_flag = True
            audio_data_flag = True
        elif self.data_flag == DataFlag.FRAME_DATA:
            frame_data_flag = True
        elif self.data_flag == DataFlag.SCREEN_DATA:
            screen_data_flag = True
        elif self.data_flag == DataFlag.AUDIO_DATA:
            audio_data_flag = True

        request = service_pb2.SpectateRequest(interval=self.interval, frame_data_flag=frame_data_flag, screen_data_flag=screen_data_flag, audio_data_flag=audio_data_flag)
        return self.stub.Spectate(request)
    
    def start(self):
        for state in self.spectate_rpc():
            flag = Flag(state.state_flag)
            if flag is Flag.INITIALIZE:
                self.handler.on_initialize(GameData.from_proto(state.game_data))
            elif flag is Flag.PROCESSING:
                self.handler.on_game_update(FrameData.from_proto(state.frame_data), ScreenData.from_proto(state.screen_data), 
                                            AudioData.from_proto(state.audio_data))
            elif flag is Flag.ROUND_END:
                self.handler.on_round_end(RoundResult.from_proto(state.round_result), False)
            elif flag is Flag.GAME_END:
                self.handler.on_round_end(RoundResult.from_proto(state.round_result), True)
    
    def close(self):
        self.channel.close()

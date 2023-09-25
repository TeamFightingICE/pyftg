from .protoc import service_pb2, service_pb2_grpc
from .enum.flag import Flag
from .struct import GameData, FrameData, ScreenData, AudioData, RoundResult
from .observer_handler import ObserverHandler
import grpc

class ObserverGateway:
    def __init__(self, handler: ObserverHandler, host='127.0.0.1', port=50051):
        self.host = host
        self.port = port
        self.channel = grpc.insecure_channel(
            target=f"{host}:{port}",
            compression=grpc.Compression.Gzip,
        )
        self.stub = service_pb2_grpc.ServiceStub(self.channel)
        self.handler = handler

    def spectate_rpc(self):
        request = service_pb2.SpectateRequest()
        return self.stub.Spectate(request)
    
    def start(self):
        for state in self.spectate_rpc():
            flag = Flag(state.state_flag)
            if flag is Flag.INITIALIZE:
                self.handler.on_initialize(GameData(state.game_data))
            elif flag is Flag.PROCESSING:
                self.handler.on_game_update(FrameData(state.frame_data), ScreenData(state.screen_data), AudioData(state.audio_data))
            elif flag is Flag.ROUND_END:
                self.handler.on_round_end(RoundResult(state.round_result), False)
            elif flag is Flag.GAME_END:
                self.handler.on_round_end(RoundResult(state.round_result), True)
    
    def close(self):
        self.channel.close()

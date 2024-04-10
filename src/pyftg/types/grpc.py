from google.protobuf.message import Message

GrpcFrameData = object
GrpcScreenData = object
GrpcAudioData = object
GrpcGameData = object
GrpcRoundResult = object


class PlayerGameState(Message):
    state_flag: int
    is_control: bool
    frame_data: GrpcFrameData
    non_delay_frame_data: GrpcFrameData
    screen_data: GrpcScreenData
    audio_data: GrpcAudioData
    game_data: GrpcGameData
    round_result: GrpcRoundResult

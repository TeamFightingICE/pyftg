from typing import NewType

from google.protobuf.message import Message

GrpcFrameData = NewType('GrpcFrameData', Message)
GrpcScreenData = NewType('GrpcScreenData', Message)
GrpcAudioData = NewType('GrpcAudioData', Message)
GrpcGameData = NewType('GrpcGameData', Message)
GrpcRoundResult = NewType('GrpcRoundResult', Message)


class PlayerGameState(Message):
    state_flag: int
    is_control: bool
    frame_data: GrpcFrameData
    non_delay_frame_data: GrpcFrameData
    screen_data: GrpcScreenData
    audio_data: GrpcAudioData
    game_data: GrpcGameData
    round_result: GrpcRoundResult

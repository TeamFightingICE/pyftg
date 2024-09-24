"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from . import enum_pb2 as enum__pb2
from . import message_pb2 as message__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rservice.proto\x12\x07service\x1a\x1bgoogle/protobuf/empty.proto\x1a\nenum.proto\x1a\rmessage.proto"s\n\x0eRunGameRequest\x12\x13\n\x0bcharacter_1\x18\x01 \x01(\t\x12\x13\n\x0bcharacter_2\x18\x02 \x01(\t\x12\x10\n\x08player_1\x18\x03 \x01(\t\x12\x10\n\x08player_2\x18\x04 \x01(\t\x12\x13\n\x0bgame_number\x18\x05 \x01(\x05"Y\n\x0fRunGameResponse\x12,\n\x0bstatus_code\x18\x01 \x01(\x0e2\x17.service.GrpcStatusCode\x12\x18\n\x10response_message\x18\x02 \x01(\t"\x83\x01\n\x0fSpectateRequest\x12\x10\n\x08interval\x18\x01 \x01(\x05\x12\x17\n\x0fframe_data_flag\x18\x02 \x01(\x08\x12\x18\n\x10screen_data_flag\x18\x03 \x01(\x08\x12\x17\n\x0faudio_data_flag\x18\x04 \x01(\x08\x12\x12\n\nkeep_alive\x18\x05 \x01(\x08"\x9b\x02\n\x12SpectatorGameState\x12%\n\nstate_flag\x18\x01 \x01(\x0e2\x11.service.GrpcFlag\x12(\n\tgame_data\x18\x02 \x01(\x0b2\x15.service.GrpcGameData\x12*\n\nframe_data\x18\x03 \x01(\x0b2\x16.service.GrpcFrameData\x12,\n\x0bscreen_data\x18\x04 \x01(\x0b2\x17.service.GrpcScreenData\x12*\n\naudio_data\x18\x05 \x01(\x0b2\x16.service.GrpcAudioData\x12.\n\x0cround_result\x18\x06 \x01(\x0b2\x18.service.GrpcRoundResult"Q\n\x11InitializeRequest\x12\x15\n\rplayer_number\x18\x01 \x01(\x08\x12\x13\n\x0bplayer_name\x18\x02 \x01(\t\x12\x10\n\x08is_blind\x18\x03 \x01(\x08")\n\x12InitializeResponse\x12\x13\n\x0bplayer_uuid\x18\x01 \x01(\t")\n\x12ParticipateRequest\x12\x13\n\x0bplayer_uuid\x18\x01 \x01(\t"\xe2\x02\n\x0fPlayerGameState\x12%\n\nstate_flag\x18\x01 \x01(\x0e2\x11.service.GrpcFlag\x12\x12\n\nis_control\x18\x02 \x01(\x08\x12*\n\nframe_data\x18\x03 \x01(\x0b2\x16.service.GrpcFrameData\x124\n\x14non_delay_frame_data\x18\x04 \x01(\x0b2\x16.service.GrpcFrameData\x12,\n\x0bscreen_data\x18\x05 \x01(\x0b2\x17.service.GrpcScreenData\x12*\n\naudio_data\x18\x06 \x01(\x0b2\x16.service.GrpcAudioData\x12(\n\tgame_data\x18\x07 \x01(\x0b2\x15.service.GrpcGameData\x12.\n\x0cround_result\x18\x08 \x01(\x0b2\x18.service.GrpcRoundResult"G\n\x0bPlayerInput\x12\x13\n\x0bplayer_uuid\x18\x01 \x01(\t\x12#\n\tinput_key\x18\x02 \x01(\x0b2\x10.service.GrpcKey2\xdc\x02\n\x07Service\x12>\n\x07RunGame\x12\x17.service.RunGameRequest\x1a\x18.service.RunGameResponse"\x00\x12E\n\x08Spectate\x12\x18.service.SpectateRequest\x1a\x1b.service.SpectatorGameState"\x000\x01\x12G\n\nInitialize\x12\x1a.service.InitializeRequest\x1a\x1b.service.InitializeResponse"\x00\x12H\n\x0bParticipate\x12\x1b.service.ParticipateRequest\x1a\x18.service.PlayerGameState"\x000\x01\x127\n\x05Input\x12\x14.service.PlayerInput\x1a\x16.google.protobuf.Empty"\x00B5\n\x06protocB\x0cServiceProtoP\x00\xaa\x02\x1aDareFightingICE.Grpc.Protob\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x06protocB\x0cServiceProtoP\x00\xaa\x02\x1aDareFightingICE.Grpc.Proto'
    _globals['_RUNGAMEREQUEST']._serialized_start = 82
    _globals['_RUNGAMEREQUEST']._serialized_end = 197
    _globals['_RUNGAMERESPONSE']._serialized_start = 199
    _globals['_RUNGAMERESPONSE']._serialized_end = 288
    _globals['_SPECTATEREQUEST']._serialized_start = 291
    _globals['_SPECTATEREQUEST']._serialized_end = 422
    _globals['_SPECTATORGAMESTATE']._serialized_start = 425
    _globals['_SPECTATORGAMESTATE']._serialized_end = 708
    _globals['_INITIALIZEREQUEST']._serialized_start = 710
    _globals['_INITIALIZEREQUEST']._serialized_end = 791
    _globals['_INITIALIZERESPONSE']._serialized_start = 793
    _globals['_INITIALIZERESPONSE']._serialized_end = 834
    _globals['_PARTICIPATEREQUEST']._serialized_start = 836
    _globals['_PARTICIPATEREQUEST']._serialized_end = 877
    _globals['_PLAYERGAMESTATE']._serialized_start = 880
    _globals['_PLAYERGAMESTATE']._serialized_end = 1234
    _globals['_PLAYERINPUT']._serialized_start = 1236
    _globals['_PLAYERINPUT']._serialized_end = 1307
    _globals['_SERVICE']._serialized_start = 1310
    _globals['_SERVICE']._serialized_end = 1658
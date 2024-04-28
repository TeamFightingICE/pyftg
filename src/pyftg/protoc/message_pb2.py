"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from . import enum_pb2 as enum__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rmessage.proto\x12\x07service\x1a\nenum.proto"G\n\x0bGrpcHitArea\x12\x0c\n\x04left\x18\x01 \x01(\x05\x12\r\n\x05right\x18\x02 \x01(\x05\x12\x0b\n\x03top\x18\x03 \x01(\x05\x12\x0e\n\x06bottom\x18\x04 \x01(\x05"\xd5\x04\n\x0eGrpcAttackData\x12.\n\x10setting_hit_area\x18\x01 \x01(\x0b2\x14.service.GrpcHitArea\x12\x17\n\x0fsetting_speed_x\x18\x02 \x01(\x05\x12\x17\n\x0fsetting_speed_y\x18\x03 \x01(\x05\x12.\n\x10current_hit_area\x18\x04 \x01(\x0b2\x14.service.GrpcHitArea\x12\x15\n\rcurrent_frame\x18\x05 \x01(\x05\x12\x15\n\rplayer_number\x18\x06 \x01(\x08\x12\x0f\n\x07speed_x\x18\x07 \x01(\x05\x12\x0f\n\x07speed_y\x18\x08 \x01(\x05\x12\x10\n\x08start_up\x18\t \x01(\x05\x12\x0e\n\x06active\x18\n \x01(\x05\x12\x12\n\nhit_damage\x18\x0b \x01(\x05\x12\x14\n\x0cguard_damage\x18\x0c \x01(\x05\x12\x18\n\x10start_add_energy\x18\r \x01(\x05\x12\x16\n\x0ehit_add_energy\x18\x0e \x01(\x05\x12\x18\n\x10guard_add_energy\x18\x0f \x01(\x05\x12\x13\n\x0bgive_energy\x18\x10 \x01(\x05\x12\x10\n\x08impact_x\x18\x11 \x01(\x05\x12\x10\n\x08impact_y\x18\x12 \x01(\x05\x12\x18\n\x10give_guard_recov\x18\x13 \x01(\x05\x12\x13\n\x0battack_type\x18\x14 \x01(\x05\x12\x11\n\tdown_prop\x18\x15 \x01(\x08\x12\x15\n\ris_projectile\x18\x16 \x01(\x08\x12\x0f\n\x07is_live\x18\x17 \x01(\x08\x12\x12\n\nempty_flag\x18\x18 \x01(\x08\x12\x12\n\nidentifier\x18\x19 \x01(\t"\xa5\x04\n\x11GrpcCharacterData\x12\x15\n\rplayer_number\x18\x01 \x01(\x08\x12\n\n\x02hp\x18\x02 \x01(\x05\x12\x0e\n\x06energy\x18\x03 \x01(\x05\x12\t\n\x01x\x18\x04 \x01(\x05\x12\t\n\x01y\x18\x05 \x01(\x05\x12\x0c\n\x04left\x18\x06 \x01(\x05\x12\r\n\x05right\x18\x07 \x01(\x05\x12\x0b\n\x03top\x18\x08 \x01(\x05\x12\x0e\n\x06bottom\x18\t \x01(\x05\x12\x0f\n\x07speed_x\x18\n \x01(\x05\x12\x0f\n\x07speed_y\x18\x0b \x01(\x05\x12!\n\x05state\x18\x0c \x01(\x0e2\x12.service.GrpcState\x12#\n\x06action\x18\r \x01(\x0e2\x13.service.GrpcAction\x12\r\n\x05front\x18\x0e \x01(\x08\x12\x0f\n\x07control\x18\x0f \x01(\x08\x12,\n\x0battack_data\x18\x10 \x01(\x0b2\x17.service.GrpcAttackData\x12\x17\n\x0fremaining_frame\x18\x11 \x01(\x05\x12\x13\n\x0bhit_confirm\x18\x12 \x01(\x08\x12\x16\n\x0egraphic_size_x\x18\x13 \x01(\x05\x12\x16\n\x0egraphic_size_y\x18\x14 \x01(\x05\x12\x18\n\x10graphic_adjust_x\x18\x15 \x01(\x05\x12\x11\n\thit_count\x18\x16 \x01(\x05\x12\x16\n\x0elast_hit_frame\x18\x17 \x01(\x05\x122\n\x11projectile_attack\x18\x18 \x03(\x0b2\x17.service.GrpcAttackData"\xcd\x01\n\rGrpcFrameData\x122\n\x0echaracter_data\x18\x01 \x03(\x0b2\x1a.service.GrpcCharacterData\x12\x1c\n\x14current_frame_number\x18\x02 \x01(\x05\x12\x15\n\rcurrent_round\x18\x03 \x01(\x05\x120\n\x0fprojectile_data\x18\x04 \x03(\x0b2\x17.service.GrpcAttackData\x12\x12\n\nempty_flag\x18\x05 \x01(\x08\x12\r\n\x05front\x18\x06 \x03(\x08"J\n\x0bGrpcFftData\x12\x1a\n\x12real_data_as_bytes\x18\x01 \x01(\x0c\x12\x1f\n\x17imaginary_data_as_bytes\x18\x02 \x01(\x0c"\'\n\x0eGrpcScreenData\x12\x15\n\rdisplay_bytes\x18\x01 \x01(\x0c"u\n\rGrpcAudioData\x12\x19\n\x11raw_data_as_bytes\x18\x01 \x01(\x0c\x12&\n\x08fft_data\x18\x02 \x03(\x0b2\x14.service.GrpcFftData\x12!\n\x19spectrogram_data_as_bytes\x18\x03 \x01(\x0c"`\n\x0cGrpcGameData\x12\x0f\n\x07max_hps\x18\x01 \x03(\x05\x12\x14\n\x0cmax_energies\x18\x02 \x03(\x05\x12\x17\n\x0fcharacter_names\x18\x03 \x03(\t\x12\x10\n\x08ai_names\x18\x04 \x03(\t"V\n\x0fGrpcRoundResult\x12\x15\n\rcurrent_round\x18\x01 \x01(\x05\x12\x15\n\rremaining_hps\x18\x02 \x03(\x05\x12\x15\n\relapsed_frame\x18\x03 \x01(\x05"V\n\x07GrpcKey\x12\t\n\x01A\x18\x01 \x01(\x08\x12\t\n\x01B\x18\x02 \x01(\x08\x12\t\n\x01C\x18\x03 \x01(\x08\x12\t\n\x01U\x18\x04 \x01(\x08\x12\t\n\x01R\x18\x05 \x01(\x08\x12\t\n\x01D\x18\x06 \x01(\x08\x12\t\n\x01L\x18\x07 \x01(\x08B5\n\x06protocB\x0cMessageProtoP\x00\xaa\x02\x1aDareFightingICE.Grpc.Protob\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'message_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x06protocB\x0cMessageProtoP\x00\xaa\x02\x1aDareFightingICE.Grpc.Proto'
    _globals['_GRPCHITAREA']._serialized_start = 38
    _globals['_GRPCHITAREA']._serialized_end = 109
    _globals['_GRPCATTACKDATA']._serialized_start = 112
    _globals['_GRPCATTACKDATA']._serialized_end = 709
    _globals['_GRPCCHARACTERDATA']._serialized_start = 712
    _globals['_GRPCCHARACTERDATA']._serialized_end = 1261
    _globals['_GRPCFRAMEDATA']._serialized_start = 1264
    _globals['_GRPCFRAMEDATA']._serialized_end = 1469
    _globals['_GRPCFFTDATA']._serialized_start = 1471
    _globals['_GRPCFFTDATA']._serialized_end = 1545
    _globals['_GRPCSCREENDATA']._serialized_start = 1547
    _globals['_GRPCSCREENDATA']._serialized_end = 1586
    _globals['_GRPCAUDIODATA']._serialized_start = 1588
    _globals['_GRPCAUDIODATA']._serialized_end = 1705
    _globals['_GRPCGAMEDATA']._serialized_start = 1707
    _globals['_GRPCGAMEDATA']._serialized_end = 1803
    _globals['_GRPCROUNDRESULT']._serialized_start = 1805
    _globals['_GRPCROUNDRESULT']._serialized_end = 1891
    _globals['_GRPCKEY']._serialized_start = 1893
    _globals['_GRPCKEY']._serialized_end = 1979
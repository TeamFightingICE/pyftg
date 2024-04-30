"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nenum.proto\x12\x07service*)\n\x0eGrpcStatusCode\x12\x0b\n\x07SUCCESS\x10\x00\x12\n\n\x06FAILED\x10\x01*b\n\x08GrpcFlag\x12\t\n\x05EMPTY\x10\x00\x12\x0e\n\nINITIALIZE\x10\x01\x12\x0e\n\nINIT_ROUND\x10\x02\x12\x0e\n\nPROCESSING\x10\x03\x12\r\n\tROUND_END\x10\x04\x12\x0c\n\x08GAME_END\x10\x05*M\n\tGrpcState\x12\x0f\n\x0bSTAND_STATE\x10\x00\x12\x10\n\x0cCROUCH_STATE\x10\x01\x12\r\n\tAIR_STATE\x10\x02\x12\x0e\n\nDOWN_STATE\x10\x03*\xd9\x06\n\nGrpcAction\x12\x0b\n\x07NEUTRAL\x10\x00\x12\t\n\x05STAND\x10\x01\x12\x10\n\x0cFORWARD_WALK\x10\x02\x12\x08\n\x04DASH\x10\x03\x12\r\n\tBACK_STEP\x10\x04\x12\n\n\x06CROUCH\x10\x05\x12\x08\n\x04JUMP\x10\x06\x12\x0c\n\x08FOR_JUMP\x10\x07\x12\r\n\tBACK_JUMP\x10\x08\x12\x07\n\x03AIR\x10\t\x12\x0f\n\x0bSTAND_GUARD\x10\n\x12\x10\n\x0cCROUCH_GUARD\x10\x0b\x12\r\n\tAIR_GUARD\x10\x0c\x12\x15\n\x11STAND_GUARD_RECOV\x10\r\x12\x16\n\x12CROUCH_GUARD_RECOV\x10\x0e\x12\x13\n\x0fAIR_GUARD_RECOV\x10\x0f\x12\x0f\n\x0bSTAND_RECOV\x10\x10\x12\x10\n\x0cCROUCH_RECOV\x10\x11\x12\r\n\tAIR_RECOV\x10\x12\x12\x0f\n\x0bCHANGE_DOWN\x10\x13\x12\x08\n\x04DOWN\x10\x14\x12\x08\n\x04RISE\x10\x15\x12\x0b\n\x07LANDING\x10\x16\x12\x0b\n\x07THROW_A\x10\x17\x12\x0b\n\x07THROW_B\x10\x18\x12\r\n\tTHROW_HIT\x10\x19\x12\x10\n\x0cTHROW_SUFFER\x10\x1a\x12\x0b\n\x07STAND_A\x10\x1b\x12\x0b\n\x07STAND_B\x10\x1c\x12\x0c\n\x08CROUCH_A\x10\x1d\x12\x0c\n\x08CROUCH_B\x10\x1e\x12\t\n\x05AIR_A\x10\x1f\x12\t\n\x05AIR_B\x10 \x12\n\n\x06AIR_DA\x10!\x12\n\n\x06AIR_DB\x10"\x12\x0c\n\x08STAND_FA\x10#\x12\x0c\n\x08STAND_FB\x10$\x12\r\n\tCROUCH_FA\x10%\x12\r\n\tCROUCH_FB\x10&\x12\n\n\x06AIR_FA\x10\'\x12\n\n\x06AIR_FB\x10(\x12\n\n\x06AIR_UA\x10)\x12\n\n\x06AIR_UB\x10*\x12\x11\n\rSTAND_D_DF_FA\x10+\x12\x11\n\rSTAND_D_DF_FB\x10,\x12\x11\n\rSTAND_F_D_DFA\x10-\x12\x11\n\rSTAND_F_D_DFB\x10.\x12\x11\n\rSTAND_D_DB_BA\x10/\x12\x11\n\rSTAND_D_DB_BB\x100\x12\x0f\n\x0bAIR_D_DF_FA\x101\x12\x0f\n\x0bAIR_D_DF_FB\x102\x12\x0f\n\x0bAIR_F_D_DFA\x103\x12\x0f\n\x0bAIR_F_D_DFB\x104\x12\x0f\n\x0bAIR_D_DB_BA\x105\x12\x0f\n\x0bAIR_D_DB_BB\x106\x12\x11\n\rSTAND_D_DF_FC\x107B2\n\x06protocB\tEnumProtoP\x00\xaa\x02\x1aDareFightingICE.Grpc.Protob\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'enum_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x06protocB\tEnumProtoP\x00\xaa\x02\x1aDareFightingICE.Grpc.Proto'
    _globals['_GRPCSTATUSCODE']._serialized_start = 23
    _globals['_GRPCSTATUSCODE']._serialized_end = 64
    _globals['_GRPCFLAG']._serialized_start = 66
    _globals['_GRPCFLAG']._serialized_end = 164
    _globals['_GRPCSTATE']._serialized_start = 166
    _globals['_GRPCSTATE']._serialized_end = 243
    _globals['_GRPCACTION']._serialized_start = 246
    _globals['_GRPCACTION']._serialized_end = 1103
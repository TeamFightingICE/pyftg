from google.protobuf.message import Message

from pyftg.models.key import Key
from pyftg.protoc import message_pb2


def convert_key_to_proto(key: Key) -> Message:
    return message_pb2.GrpcKey(A=key.A, B=key.B, C=key.C, U=key.U, D=key.D, L=key.L, R=key.R)

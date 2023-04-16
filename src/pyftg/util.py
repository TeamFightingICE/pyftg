from .struct import Key
from .aiinterface import AIInterface
from .protoc import message_pb2

def convert_key(key: Key) -> message_pb2.GrpcKey:
    return message_pb2.GrpcKey(A=key.A, B=key.B, C=key.C, U=key.U, D=key.D, L=key.L, R=key.R)

def load_ai(ai_path: str) -> AIInterface:
    path = ai_path.split('.')
    module_name, class_name = path[0], path[int(len(path) == 2)]
    return getattr(__import__(module_name), class_name)()

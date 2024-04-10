from dataclasses import dataclass

from google.protobuf.message import Message

from pyftg.models.base_model import BaseModel


@dataclass
class Key(BaseModel):
    A: bool = False
    B: bool = False
    C: bool = False
    U: bool = False
    R: bool = False
    D: bool = False
    L: bool = False

    def empty(self):
        self.A = False
        self.B = False
        self.C = False
        self.U = False
        self.R = False
        self.D = False
        self.L = False
    
    def to_dict(self):
        return {
            "A": self.A,
            "B": self.B,
            "C": self.C,
            "U": self.U,
            "R": self.R,
            "D": self.D,
            "L": self.L
        }

    @classmethod
    def from_dict(cls, data_obj: dict):
        return Key(
            A=data_obj["A"],
            B=data_obj["B"],
            C=data_obj["C"],
            U=data_obj["U"],
            R=data_obj["R"],
            D=data_obj["D"],
            L=data_obj["L"]
        )
    
    @classmethod
    def from_proto(cls, proto_obj: Message):
        return Key(
            A=proto_obj.A,
            B=proto_obj.B,
            C=proto_obj.C,
            U=proto_obj.U,
            R=proto_obj.R,
            D=proto_obj.D,
            L=proto_obj.L
        )
    
    @classmethod
    def get_default_instance(cls):
        return Key(A=False, B=False, C=False, U=False, R=False, D=False, L=False)

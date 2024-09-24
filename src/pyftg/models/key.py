from dataclasses import dataclass

from google.protobuf.message import Message

from pyftg.models.base_model import BaseModel


@dataclass
class Key(BaseModel):
    """
    Key (BaseModel): Key data class.
    """

    A: bool = False
    """
    A (bool): A key state. True if pressed, otherwise False
    """
    B: bool = False
    """
    B (bool): B key state. True if pressed, otherwise False
    """
    C: bool = False
    """
    C (bool): C key state. True if pressed, otherwise False
    """
    U: bool = False
    """
    U (bool): U key state. True if pressed, otherwise False
    """
    R: bool = False
    """
    R (bool): R key state. True if pressed, otherwise False
    """
    D: bool = False
    """
    D (bool): D key state. True if pressed, otherwise False
    """
    L: bool = False
    """
    L (bool): L key state. True if pressed, otherwise False
    """

    def empty(self):
        """
        Reset all key states to False.
        """
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

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class BaseModel(ABC):
    @abstractmethod
    def to_dict(self) -> dict:
        pass

    @classmethod
    @abstractmethod
    def from_dict(cls, data_obj: dict):
        pass

    @classmethod
    @abstractmethod
    def get_default_instance(cls):
        pass

from abc import ABC, abstractmethod
from dataclasses import dataclass

import orjson


@dataclass
class BaseModel(ABC):
    def to_json(self) -> bytes:
        return orjson.dumps(self)

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

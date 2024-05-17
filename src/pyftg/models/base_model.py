from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class BaseModel(ABC):
    @abstractmethod
    def to_dict(self) -> dict:
        """
        Convert data class to dictionary.

        Returns:
            dict: Dictionary representation of the data class.
        """
        pass

    @classmethod
    @abstractmethod
    def from_dict(cls, data_obj: dict):
        """
        Create data class from dictionary.

        Args:
            data_obj (dict): Dictionary to convert to data class.

        Returns:
            BaseModel: Data class created from dictionary.
        """
        pass

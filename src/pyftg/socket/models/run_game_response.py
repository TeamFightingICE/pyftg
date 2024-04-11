from dataclasses import dataclass

from pyftg.models.base_model import BaseModel
from pyftg.models.enums.status_code import StatusCode


@dataclass
class RunGameResponse(BaseModel):
    status_code: StatusCode
    response_message: str

    def to_dict(self) -> dict:
        return {
            'status_code': self.status_code.value,
            'response_message': self.response_message,
        }
    
    @classmethod
    def from_dict(cls, data_obj: dict):
        return RunGameResponse(
            status_code=StatusCode(data_obj['status_code']),
            response_message=data_obj['response_message'],
        )
    
    @classmethod
    def get_default_instance(cls):
        return RunGameResponse(
            status_code=StatusCode.UNKNOWN,
            response_message='',
        )

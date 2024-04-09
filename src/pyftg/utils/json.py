import orjson

from pyftg.models.base_model import BaseModel


def json_dumps(model: BaseModel) -> bytes:
    return orjson.dumps(model)

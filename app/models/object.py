from pydantic import BaseModel
from typing import Dict, Any


class ObjectModel(BaseModel):
    key: str
    value: Dict[str, Any]
    ttl: int

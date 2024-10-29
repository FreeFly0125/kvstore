from pydantic import BaseModel
from typing import Dict, Any, Optional


class ObjectModel(BaseModel):
    key: str
    value: Dict[str, Any]
    ttl: Optional[int]

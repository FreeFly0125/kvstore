from pydantic import BaseModel
from typing import Optional


class TenantModel(BaseModel):
    name: str
    cap_limit: Optional[int] = None
    data_ttl: Optional[int] = None

from pydantic import BaseModel


class ObjectModel(BaseModel):
    key: str
    value: object
    ttl: int

from fastapi import APIRouter
from app.models.object import ObjectModel
from app.services import objectService as ObjectService
from app.api.util import response

object_route = APIRouter()


@object_route.get("/{id}")
def get_object_info(id: str):
    pass


@object_route.post("/")
def insert_new_object(obj: ObjectModel):
    success = ObjectService.insert_new_data(
        key=obj.key, value=obj.value, data_ttl=obj.ttl
    )
    return response(success=success)

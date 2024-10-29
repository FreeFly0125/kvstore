from fastapi import APIRouter, Depends
from app.models.object import ObjectModel
from app.services import objectService as ObjectService
from app.api.util import response
from app.api.validator import verify_token
from typing import List

object_route = APIRouter()


@object_route.get("/object/{oid}")
def get_object_info(oid: str, tenant_id: str = Depends(verify_token)):
    return ObjectService.get_data_info(oid=oid)


@object_route.post("/object")
def insert_new_object(obj: ObjectModel, tenant_id: str = Depends(verify_token)):
    success = ObjectService.insert_new_data(info=obj, tenant_id=tenant_id)
    return response(success=success)


@object_route.post("/batch/object")
def batch_insert_object(
    objs: List[ObjectModel], tenant_id: str = Depends(verify_token)
):
    success = ObjectService.batch_insert_data(objs, tenant_id=tenant_id)
    return response(success=success)


@object_route.delete("/object/{oid}")
def remove_object_info(oid: str, tenant_id: str = Depends(verify_token)):
    success = ObjectService.delete_data_info(oid=oid, tid=tenant_id)
    return response(success=success)

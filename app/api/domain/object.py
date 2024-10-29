from fastapi import APIRouter, Depends
from app.models.object import ObjectModel
from app.services import objectService as ObjectService
from app.services import tenantService as TenantService
from app.api.util import response
from app.api.validator import verify_token
from app.api import error
from typing import List

object_route = APIRouter()


@object_route.get("/object/{key}")
def get_object_info(key: str, tenant_id: str = Depends(verify_token)):
    data_obj = ObjectService.get_data_info(key=key, tid=tenant_id)
    if not data_obj:
        raise error.DataNotExistException()
    return data_obj


@object_route.post("/object")
def insert_new_object(obj: ObjectModel, tenant_id: str = Depends(verify_token)):
    former_obj = ObjectService.get_data_info(key=obj.key, tid=tenant_id)
    if former_obj:
        raise error.KeyAlreadyExistException()
    (capSize, curCount) = TenantService.get_current_capacity(tid=tenant_id)
    if capSize == curCount:
        raise error.CapacityFilledException()
    success = ObjectService.insert_new_data(info=obj, tenant_id=tenant_id)
    return response(success=success)


@object_route.post("/batch/object")
def batch_insert_object(
    objs: List[ObjectModel], tenant_id: str = Depends(verify_token)
):
    (capSize, curCount) = TenantService.get_current_capacity(tid=tenant_id)
    if capSize == curCount:
        raise error.CapacityFilledException()
    if capSize < curCount + len(objs):
        raise error.InsufficientCapacityException()
    success = ObjectService.batch_insert_data(objs, tenant_id=tenant_id)
    return response(success=success)


@object_route.delete("/object/{key}")
def remove_object_info(key: str, tenant_id: str = Depends(verify_token)):
    success = ObjectService.delete_data_info(key=key, tid=tenant_id)
    return response(success=success)

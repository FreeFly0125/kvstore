from fastapi import APIRouter
from app.services import tenantService as TenantService
from app.models.tenant import TenantModel
from app.api.validator import validate
from app.api.util import response
from app.api import error

import uuid
import jwt
import os
import time
from dotenv import load_dotenv

load_dotenv()
secret_key = os.getenv("SECRET_KEY")

tenant_route = APIRouter()


@tenant_route.get("/")
def tenant_get_data():
    return TenantService.get_all_tenants()


@tenant_route.get("/{tenant_id}")
def tenant_get_individual(tenant_id: str):
    return TenantService.get_single_tenant_with_tid(tenant_id)


@tenant_route.post("/signup")
@validate("tenant_register")
def tenant_sign_up(tenant: TenantModel):
    tenant_id = str(uuid.uuid4())
    success = TenantService.insert_new_tenant(tenant=tenant, tid=tenant_id)
    return response(success=success)


@tenant_route.post("/signin")
@validate("tenant_login")
def tenant_sign_in(tenant: TenantModel):
    tenant_info = TenantService.get_single_tenant_with_name(tenant.name)
    if not tenant_info:
        raise error.TenantNotFoundException()
    payload = {
        "tenant_name": tenant_info.name,
        "tenant_id": tenant_info.tenantID,
        "data_ttl": tenant_info.dataTtl,
        "exp": time.time() + 60 * 30,
    }
    token = jwt.encode(payload=payload, key=secret_key, algorithm="HS256")
    return response(payload={"token": token})

from fastapi import APIRouter
from app.api.domain.tenant import tenant_route

api_router = APIRouter()


@api_router.get("/health_check")
def health_check():
    return {"Message": "Server is Running"}


api_router.include_router(tenant_route, prefix="/tenant")

from app.db.dbconnect import SessionLocal
from app.db.schemas import TenantSchema
from app.models.tenant import TenantModel
from app.api import error

dbHandler = SessionLocal()


def get_all_tenants():
    return dbHandler.query(TenantSchema).all()


def get_single_tenant_with_name(name: str):
    try:
        tenant = dbHandler.query(TenantSchema).filter(TenantSchema.name == name).first()
        return tenant
    except Exception:
        raise error.TenantFetchFailException()


def get_single_tenant_with_tid(tid: str):
    try:
        tenant = (
            dbHandler.query(TenantSchema).filter(TenantSchema.tenantID == tid).first()
        )
        return tenant
    except Exception:
        raise error.TenantFetchFailException()


def insert_new_tenant(tenant: TenantModel, tid: str):
    try:
        new_tenant = TenantSchema(
            tenantID=tid,
            name=tenant.name,
            capSize=tenant.cap_limit,
            curCount=0,
        )
        dbHandler.add(new_tenant)
        dbHandler.commit()
        return True
    except Exception as e:
        raise error.TenantRegisterFailException(e.message)


def delete_tenant(tid: str):
    try:
        tenant = (
            dbHandler.query(TenantSchema).filter(TenantSchema.tenantID == tid).first()
        )
        if tenant:
            dbHandler.delete(tenant)
            dbHandler.commit()
            return True
        else:
            raise error.TenantNotFoundException()
    except Exception as e:
        raise error.TenantDeleteFailException(e.message)


def get_current_capacity(tid: str):
    try:
        tenant = (
            dbHandler.query(TenantSchema).filter(TenantSchema.tenantID == tid).first()
        )
        if not tenant:
            raise error.TenantNotFoundException()
        return (tenant.capSize, tenant.curCount)
    except Exception as e:
        raise error.TenantCapacityFailException(e.message)
